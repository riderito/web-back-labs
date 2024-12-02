from flask import Blueprint, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path


lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'alexey_stepuk_knowledge_base',
            user = 'alexey_stepuk_knowledge_base',
            password = '123'
        )
        cur = conn.cursor(cursor_factory =  RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def populate_offices():
    conn, cur = db_connect()
    # Очистка таблицы перед добавлением новых данных
    cur.execute("DELETE FROM offices;")
    
    # Заполнение таблицы офисами
    for i in range(1, 11):
        office_number = i
        price = 730 + i**2
        tenant = None  # По умолчанию офис свободен
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                "INSERT INTO offices (number, tenant_login, price) VALUES (%s, %s, %s);",
            (office_number, tenant, price))
        else:
            cur.execute(
                "INSERT INTO offices (number, tenant_login, price) VALUES (?, ?, ?);",
            (office_number, tenant, price))

    db_close(conn, cur)

if __name__ == "__main__":
    populate_offices()

@lab6.route('/lab6/json-rpc-api/', methods = ['POST'])
def api():
    data = request.json
    request_id = data.get('id', None)
    method = data.get('method')
    params = data.get('params', None)
    login = session.get('login')

    if method == 'info':
        try:
            conn, cur = db_connect()
            # Получение списка офисов
            cur.execute("SELECT number, price, tenant_login FROM offices;")
            offices = cur.fetchall()
            result = [
                {
                    'number': office['number'],
                    'price': office['price'],
                    'tenant': office['tenant_login']
                } for office in offices
            ]
            
            return {'jsonrpc': '2.0', 'result': result, 'id': request_id}
        finally:
            db_close(conn, cur)

    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {'code': 1, 'message': 'Unauthorized'},
            'id': request_id
        }

    if method == 'get_total_price':
        try:
            conn, cur = db_connect()
            # Получение общей стоимости аренды текущего пользователя
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute(
                    "SELECT SUM(price) AS total_price FROM offices WHERE tenant_login = %s;",
                (login,))
            else:
                cur.execute(
                    "SELECT SUM(price) AS total_price FROM offices WHERE tenant_login = ?;",
                (login,))

            total_price = cur.fetchone()['total_price'] or 0
            
            return {'jsonrpc': '2.0', 'result': total_price, 'id': request_id}
        finally:
            db_close(conn, cur)

    if method == 'booking':
        try:
            conn, cur = db_connect()
            # Аренда офиса
            office_number = params
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute(
                    "SELECT tenant_login FROM offices WHERE number = %s;", (office_number,))
            else:
                cur.execute(
                "SELECT tenant_login FROM offices WHERE number = ?;", (office_number,))
                
            office = cur.fetchone()

            if not office:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 5, 'message': 'Office not found'},
                    'id': request_id
                }
            if office['tenant_login']:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 2, 'message': 'Already booked'},
                    'id': request_id
                }

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute(
                    "UPDATE offices SET tenant_login = %s WHERE number = %s;", (login, office_number))
            else:
                cur.execute(
                "UPDATE offices SET tenant_login = ? WHERE number = ?;", (login, office_number))
            return {'jsonrpc': '2.0', 'result': 'success', 'id': request_id}
        finally:
            db_close(conn, cur)

    if method == 'cancellation':
        # Освобождение офиса
        office_number = params
        try:
            conn, cur = db_connect()

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute(
                    "SELECT tenant_login FROM offices WHERE number = %s;", (office_number,))
            else:
                cur.execute(
                "SELECT tenant_login FROM offices WHERE number = ?;", (office_number,))
            office = cur.fetchone()
            
            if not office:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 5, 'message': 'Office not found'},
                    'id': request_id
                }
            if not office['tenant_login']:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 3, 'message': 'Office is not rented'},
                    'id': request_id
                }
            if office['tenant_login'] != login:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 4, 'message': 'Cannot cancel someone\'s rental'},
                    'id': request_id
                }

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute(
                    "UPDATE offices SET tenant_login = NULL WHERE number = %s;",
                (office_number,))
            else:
                cur.execute(
                "UPDATE offices SET tenant_login = NULL WHERE number = ?;",
                (office_number,))

            return {'jsonrpc': '2.0', 'result': 'success', 'id': request_id}
        finally:
            db_close(conn, cur)
    
    return {
        'jsonrpc': '2.0',
        'error': {'code': -32601, 'message': 'Method not found'},
        'id': request_id
    }
    
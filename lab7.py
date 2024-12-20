from flask import Blueprint, render_template, request, abort, jsonify, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path
from datetime import datetime

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


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


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM films;")
    else:
        cur.execute("SELECT * FROM films;")
    
    films = cur.fetchall()
    db_close(conn, cur)
    return jsonify([dict(film) for film in films])


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM films WHERE id = %s;", (id,))
    else:
        cur.execute("SELECT * FROM films WHERE id = ?;", (id,))
    
    film = cur.fetchone()
    db_close(conn, cur)

    if film:
        return jsonify(dict(film))
    else:
        abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM films WHERE id = %s RETURNING id;", (id,))
    else:
        cur.execute("DELETE FROM films WHERE id = ?;", (id,))
    
    deleted = cur.rowcount
    db_close(conn, cur)

    if deleted > 0:
        return '', 204
    else:
        abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)
    
    # Проверяем оригинальное название
    if not film.get('title') and not film['title_ru']:
        return {'error': 'Название на оригинальном языке обязательно, если нет и русского названия'}, 400
    
    # Проверяем, что русское название заполнено
    if not film.get('title_ru'):
        return {'error': 'Русское название обязательно'}, 400
    
    # Если оригинальное название пустое, копируем русское
    if not film.get('title'):
        film['title'] = film['title_ru']

    # Вычисляем текущий год
    current_year = datetime.now().year

    # Преобразуем год в число, если он передан как строка
    try:
        year = int(film.get('year'))
    except ValueError:
        return {'error': 'Год должен быть числом'}, 400
    
    # Проверяем год выпуска
    if year < 1895 or year > current_year:
        return {'error': f'Год должен быть от 1895 до {current_year}'}, 400

    # Проверяем описание
    if not film.get('description') or len(film['description']) > 2000:
        return {'error': 'Описание обязательно и не должно превышать 2000 символов'}, 400
    
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(
            "UPDATE films SET title = %s, title_ru = %s, year = %s, description = %s WHERE id = %s;",
            (film['title'], film['title_ru'], film['year'], film['description'], id)
        )
    else:
        cur.execute(
            "UPDATE films SET title = ?, title_ru = ?, year = ?, description = ? WHERE id = ?;",
            (film['title'], film['title_ru'], film['year'], film['description'], id)
        )
    
    db_close(conn, cur)
    return jsonify(film)


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)

    # Проверяем оригинальное название
    if not film.get('title') and not film['title_ru']:
        return {'error': 'Название на оригинальном языке обязательно, если нет и русского названия'}, 400
    
    # Проверяем, что русское название заполнено
    if not film.get('title_ru'):
        return {'error': 'Русское название обязательно'}, 400
    
    # Если оригинальное название пустое, копируем русское
    if not film.get('title'):
        film['title'] = film['title_ru']

    # Вычисляем текущий год
    current_year = datetime.now().year

    # Преобразуем год в число, если он передан как строка
    try:
        year = int(film.get('year'))
    except ValueError:
        return {'error': 'Год должен быть числом'}, 400
    
    # Проверяем год выпуска
    if year < 1895 or year > current_year:
        return {'error': f'Год должен быть от 1895 до {current_year}'}, 400

    # Проверяем описание
    if not film.get('description') or len(film['description']) > 2000:
        return {'error': 'Описание обязательно и не должно превышать 2000 символов'}, 400
    

    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(
            "INSERT INTO films (title, title_ru, year, description) VALUES (%s, %s, %s, %s) RETURNING id;",
            (film['title'], film['title_ru'], film['year'], film['description'])
        )
        new_id = cur.fetchone()['id']
    else:
        cur.execute(
            "INSERT INTO films (title, title_ru, year, description) VALUES (?, ?, ?, ?);",
            (film['title'], film['title_ru'], film['year'], film['description'])
        )
        new_id = cur.lastrowid

    db_close(conn, cur)
    return jsonify({"id": new_id}), 201


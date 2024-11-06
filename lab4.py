from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/slozh-form')
def slozh_form():
    return render_template('lab4/slozh-form.html')


@lab4.route('/lab4/slozh', methods = ['POST'])
def slozh():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 0
    if x2 == '': x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/slozh.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/umn-form')
def umn_form():
    return render_template('lab4/umn-form.html')


@lab4.route('/lab4/umn', methods = ['POST'])
def umn():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 1
    if x2 == '': x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/umn.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/diff-form')
def diff_form():
    return render_template('lab4/diff-form.html')


@lab4.route('/lab4/diff', methods = ['POST'])
def diff():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/diff.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/diff.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/step-form')
def step_form():
    return render_template('lab4/step-form.html')


@lab4.route('/lab4/step', methods = ['POST'])
def step():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/step.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 != 0 and x2 != 0:
        result = x1 ** x2
        return render_template('lab4/step.html', x1=x1, x2=x2, result=result)
    return render_template('lab4/step.html', error='Оба поля равны нулю!')


tree_count = 0


@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Levy', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Charlton', 'gender': 'male'},
    {'login': 'mila', 'password': 'fffddd', 'name': 'Mila Kunis', 'gender': 'female'},
    {'login': 'george', 'password': '135', 'name': 'George Bush', 'gender': 'male'},
]


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized=True
            name = session.get('name', '')
        else:
            authorized=False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    elif not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        # Получаем температуру
        temperature = request.form.get('temperature')
        # Проверяем, была ли введена температура
        if temperature is None or temperature.strip() == '':
            message = "Ошибка: не задана температура"
            snow = 0
        else:
            # Преобразуем температуру в число
            temperature = int(temperature)
            
            # Проверка диапазона температуры
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
                snow = 0
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
                snow = 0
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
                snow = 3
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
                snow = 2
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С"
                snow = 1

        return render_template('/lab4/fridge.html', message=message, snow=snow)

    # Обработка GET-запроса для загрузки страницы
    return render_template('/lab4/fridge.html', message=None, snow=0)


# Цены на зерно в рублях за тонну
grain_prices = {
    'ячмень': 12345,
    'овёс': 8522,
    'пшеница': 8722,
    'рожь': 14111
}

@lab4.route('/lab4/grain-order', methods=['GET', 'POST'])
def grain_order():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        # Проверка, введен ли вес и корректен ли он
        if not weight:
            error = "Ошибка: не указан вес"
            return render_template('/lab4/grain-order.html', error=error)
        
        weight = float(weight)
        if weight <= 0:
            error = "Ошибка: вес должен быть положительным числом"
            return render_template('/lab4/grain-order.html', error=error)

        # Проверка на наличие доступного объема зерна
        if weight > 500:
            error = "Ошибка: такого объема сейчас нет в наличии"
            return render_template('/lab4/grain-order.html', error=error)

        # Расчет стоимости
        price_per_ton = grain_prices.get(grain_type)
        if not price_per_ton:
            error = "Ошибка: неверный тип зерна"
            return render_template('/lab4/grain-order.html', error=error)
        
        total_cost = weight * price_per_ton
        discount = 0

        # Применение скидки за заказ более 50 тонн
        if weight > 50:
            discount = 0.1  # 10%
            total_cost *= (1 - discount)

        # Формирование сообщения о заказе
        message = (f"Заказ успешно сформирован. Вы заказали {grain_type}. "
                   f"Вес: {weight:.2f} т. Сумма к оплате: {total_cost:.2f} руб")
        
        if discount > 0:
            message += f" (применена скидка {int(discount * 100)}% за большой объем)"

        return render_template('/lab4/grain-order.html', message=message)

    # GET-запрос для отображения формы заказа
    return render_template('/lab4/grain-order.html')

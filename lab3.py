from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Кофе - 120 руб, черный чай - 80 руб, зеленый чай - 70 руб
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока дает плюсом 30 руб, а сахара - 10 руб
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        color = request.form.get('color')
        background_color = request.form.get('background_color')
        font_size = request.form.get('font_size')
        text_align = request.form.get('text_align')

        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if text_align:
            resp.set_cookie('text_align', text_align)
        return resp

    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    text_align = request.cookies.get('text_align')
    resp = make_response(render_template('lab3/settings.html', color=color, background_color=background_color,
                                         font_size=font_size, text_align=text_align))
    return resp


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    # Создаем ответ с перенаправлением на страницу третьей лабы
    resp = make_response(redirect('/lab3/'))
    # Удаляем каждую куку, установленную в /lab3/settings
    resp.delete_cookie('color')
    resp.delete_cookie('background_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('text_align')
    return resp


@lab3.route('/lab3/ticket-form')
def ticket_form():
    return render_template('lab3/ticket_form.html')


@lab3.route('/lab3/ticket-result', methods=['POST'])
def ticket_result():
    fio = request.form.get('fio')
    age = int(request.form.get('age'))
    departure = request.form.get('departure')
    destination = request.form.get('destination')
    date = request.form.get('date')
    berth = request.form.get('berth')
    bedding = 'bedding' in request.form
    luggage = 'luggage' in request.form
    insurance = 'insurance' in request.form
    # Расчет стоимости
    price = 700 if age < 18 else 1000  # Детский или взрослый билет
    # Добавка за нижнюю или нижнюю боковую полку
    if berth == 'lower' or berth == 'side_lower':
        price += 100
    # Добавка за белье
    if bedding:
        price += 75
    # Добавка за багаж
    if luggage:
        price += 250
    # Добавка за страховку
    if insurance:
        price += 150
    # Определяем тип билета
    ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
    return render_template('lab3/ticket_result.html', fio=fio, age=age, departure=departure,
                           destination=destination, date=date, berth=berth,
                           bedding=bedding, luggage=luggage, insurance=insurance,
                           ticket_type=ticket_type, price=price)

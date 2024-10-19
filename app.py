from flask import Flask, redirect, url_for, render_template, request
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab2">Вторая лабораторная</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Степук Алексей Витальевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@app.route('/lab2/a')
def a():
    return 'без слэша'


@app.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = [
    {'name': 'роза', 'price': 250},
    {'name': 'тюльпан', 'price': 180},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 130},
    {'name': 'георгин', 'price': 640},
    {'name': 'гортензия', 'price': 204},
]


@app.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('flowers.html', flower_list=flower_list, flower_count=flower_count)


@app.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    if flower_id >= len(flower_list):
        return render_template('404.html', message="Цветка с таким номером нет"), 404
    else:
        flower_list.pop(flower_id)
        return redirect(url_for('list_flowers'))


@app.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()  # Очищаем список
    return render_template('flowers.html', flower_list=flower_list, flower_count=len(flower_list))


@app.route('/lab2/add_flower/')
def add_flower():
    name = request.args.get('name')
    price = request.args.get('price')
    if name and price:
        flower_list.append({"name": name, "price": price})
        return render_template('flowers.html', flower_list=flower_list, flower_count=len(flower_list))
    return 'Вы не задали имя цветка или его цену', 400


@app.route('/lab2/example')
def example():
    name, number_lab, group_student, number_course = 'Алексей Степук', 2, 'ФБИ-24', 3
    fruits = [
        {'name': 'яблоки', 'price': 101},
        {'name': 'груши', 'price': 121},
        {'name': 'апельсины', 'price': 81},
        {'name': 'мандарины', 'price': 96},
        {'name': 'манго', 'price': 322}
    ]
    return render_template('example.html', name=name, number_lab=number_lab,
                           group_student=group_student, number_course=number_course,
                           fruits=fruits)


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum = a + b
    razn = a - b
    umn = a * b
    dele = a / b if b != 0 else 'деление на 0'
    step = a ** b
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчёт с параметрами:</h1>
        <p>Сумма: {a} + {b} = {sum}</p>
        <p>Разность: {a} - {b} = {razn}</p>
        <p>Умножение: {a} X {b} = {umn}</p>
        <p>Деление: {a} / {b} = {dele}</p>
        <p>Возведение в степень: {a}<sup>{b}</sup> = {step}</p>
    </body>
</html>
'''


# Функция Flask redirect перенаправляет пользователя на другой маршрут
@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')


@app.route('/lab2/calc/<int:a>')
def calc_redirect(a):
    return redirect(url_for('calc', a=a, b=1))


books = [
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Роман", "pages": 288},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Роман в стихах", "pages": 352},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1274},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 640},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 528},
    {"author": "Маргарет Митчелл", "title": "Унесённые ветром", "genre": "Роман", "pages": 1472},
    {"author": "Антон Чехов", "title": "Вишнёвый сад", "genre": "Пьеса", "pages": 128},
    {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 432},
    {"author": "Николай Гоголь", "title": "Мёртвые души", "genre": "Сатира", "pages": 425},
    {"author": "Максим Горький", "title": "Мать", "genre": "Роман", "pages": 370}
]


@app.route('/lab2/books/')
def book_list():
    return render_template('books.html', books=books)


movies = [
    {"title": "Назад в будущее", "description": "Фантастическое приключение о путешествиях во времени.", "image": "back_to_the_future.jpg"},
    {"title": "Крёстный отец", "description": "Эпическая криминальная сага о мафиозной семье Корлеоне.", "image": "godfather.jpg"},
    {"title": "Матрица", "description": "Фантастический боевик о мире, где реальность — это иллюзия.", "image": "matrix.jpg"},
    {"title": "Бойцовский клуб", "description": "Первое правило Бойцовского клуба — никому не рассказывать о Бойцовском клубе!", "image": "fight_club.jpg"},
    {"title": "Интерстеллар", "description": "Научно-фантастический фильм о путешествиях в дальний космос.", "image": "interstellar.jpg"}
]


@app.route('/lab2/movies/')
def movie_list():
    return render_template('movies.html', movies=movies)

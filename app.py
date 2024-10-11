from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

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

@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Степук Алексей Витальевич. Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div style="margin: 10px 0;">
            Flask — фреймворк для создания веб-приложений на языке<br>
            программирования Python, использующий набор инструментов<br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так<br>
            называемых микрофреймворков — минималистичных каркасов<br>
            веб-приложений, сознательно предоставляющих лишь самые ба-<br>
            зовые возможности.
        </div>
        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>

        <div style="margin: 10px 0;">
            <ul>
                <li><a href="/lab1/oak">/lab1/oak - Дуб</a></li>
                <li><a href="/lab1/student">/lab1/student - Студент</a></li>
                <li><a href="/lab1/python">/lab1/python - Python</a></li>
                <li><a href="/lab1/holland">/lab1/holland - Том Холланд</a></li>
            <ul>
        </div>
            
        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Дуб</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <div>
                <h1>Дуб</h1>
                <img src="''' + url_for('static', filename='oak.jpg') + '''">
            </div>
        </main>
        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div>
                <h1>Степук Алексей Витальевич</h1>
                <img src="''' + url_for('static', filename='logo_nstu.png') + '''">
            </div>
        </main>

        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Python</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Python</h1>

                <p>
                    <b>Python</b> — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и для многих платформ: начиная с iOS и Android и заканчивая серверными операционными системами.
                </p>

                <h2>Как и где применяется Python</h2> 

                <p>
                    Это интерпретируемый язык, а не компилируемый, как C++ или Java. Программа на Python представляет собой обычный текстовый файл. Код можно писать практически в любом редакторе или использовать специальные IDE:
                </p>

                <ol>
                    <li>PyCharm — мощная среда разработки от JetBrains.</li>
                    <li>Spyder — IDE, оптимизированная для работы в Data Science. Идёт в пакете с Anaconda.</li>
                    <li>IDLE — стандартный текстовый редактор в составе языка.</li>
                    <li>SublimeText — текстовый редактор с множеством плагинов.</li>
                    <li>Visual Studio Code — популярный текстовый редактор от Microsoft.</li>
                </ol>

                <p>
                    Python можно встретить почти везде: в вебе, мобильных и десктопных приложениях, а также в играх. На нём пишут нейросети, проводят научные исследования и тестируют программы. Поговорим подробнее об основных сферах его применения.
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='python.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/holland")
def holland():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Том Холланд</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Том Холланд</h1>

                <p>
                    <b>То́мас Стэ́нли (Том) Хо́лланд</b> (англ. Thomas Stanley «Tom» Holland; род. 1 июня 1996, Кингстон-апон-Темс, Лондон, Великобритания) — британский актёр. Широкую известность получил после исполнения роли Человека-паука в кинематографической вселенной Marvel.
                </p>

                <p>
                    Выпускник Лондонской школы исполнительского искусства и технологий (BRIT School) начал свой актёрский путь на сцене в одиннадцатилетнем возрасте с исполнения главной роли Билли Эллиота в одноимённом мюзикле в лондонском театре Вест-Энда, в котором Холланд выступал с 2008 по 2010 год. Первая известность встретила пятнадцатилетнего Томаса после исполнения главной роли в картине 2012 года «Невозможное», которая принесла ему награду Лондонского кружка кинокритиков в категории «Самый многообещающий молодой английский актёр».
                </p>

                <p>
                    В 2017 году двадцатилетний Томас Холланд стал третьим самым юным лауреатом награды Британской академии «BAFTA» в категории «Восходящая звезда».
                </p>

                <h2>Личная жизнь</h2>

                <p>
                    Проживает в Лондоне в районе Кингстон-апон-Темс рядом с домом своих родителей и младших братьев. Томас — активный гимнаст и танцор. У него есть голубой Стаффордширский бультерьер по имени Тесса. В семилетнем возрасте у Тома была диагностирована дислексия.
                </p>

                <p>
                    В ноябре 2021 года Холланд подтвердил свои отношения с партнёршей по серии фильмов «Человек-паук» Зендеей. Они появились как пара на красной ковровой дорожке в ноябре 2021 года, когда начался пресс-тур для фильма «Человек-паук: Нет пути домой».
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='holland.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

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

@app.route('/lab2/add_flower')
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

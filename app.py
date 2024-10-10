from flask import Flask, redirect, url_for, render_template
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

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'такого цветка нет', 404
    else:
        return 'цветок: ' + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Алексей Степук'
    number_lab = 2
    group_student = 'ФБИ-24'
    number_course = 3
    return render_template('example.html', name=name, number_lab=number_lab,
                           group_student=group_student, number_course=number_course)

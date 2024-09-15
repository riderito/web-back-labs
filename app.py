from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Степук Алексей, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

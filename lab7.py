from flask import Blueprint, render_template, request, abort, jsonify


lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "The Proposal",
        "title_ru": "Предложение",
        "year": 2009,
        "description": "Главная героиня фильма – ответственная начальница, которой грозит высылка в Канаду. \
        Ради того, чтобы избежать ссылки в край озер, героиня готова на все – даже фиктивно выскочить замуж за своего молодого ассистента..."
    },
    {
        "title": "Blended",
        "title_ru": "Смешанные",
        "year": 2014,
        "description": "После катастрофического свидания «вслепую»  родители-одиночки Лорен и Джим согласны только в одном: \
        они не хотят больше видеть друг друга никогда! Полагая, что их знакомство окончено, обе семьи пользуются удобным случаем \
        и отправляются в идеальный отпуск с детьми. А оказываются в одних и тех же гостиничных апартаментах на роскошном \
        южноафриканском курорте аж на целую неделю."
    },
    {
        "title": "Just Go with It",
        "title_ru": "Притворись моей женой",
        "year": 2011,
        "description": "Пластический хирург влюблён в молоденькую учительницу. Чтобы выпутаться из неловкой ситуации, \
        в которую попал по собственной глупости, он просит свою преданную ассистентку притвориться его женой, с которой \
        он якобы собирается развестись. Один обман следует за другим, и вот в историю втянуты уже и дети его коллеги, \
        и теперь все они отправляются на уикенд на Гавайи."
    },
    {
        "title": "Avengers: Endgame",
        "title_ru": "Мстители: Финал",
        "year": 2019,
        "description": "Оставшиеся в живых члены команды Мстителей и их союзники должны разработать новый план, \
        который поможет противостоять разрушительным действиям могущественного титана Таноса. \
        После наиболее масштабной и трагической битвы в истории они не могут допустить ошибку."
    },
    {
        "title": "Spider-Man: No Way Home",
        "title_ru": "Человек-паук: Нет пути домой",
        "year": 2021,
        "description": "Жизнь и репутация Питера Паркера оказываются под угрозой, поскольку Мистерио раскрыл \
        всему миру тайну личности Человека-паука. Пытаясь исправить ситуацию, Питер обращается за помощью \
        к Стивену Стрэнджу, но вскоре всё становится намного опаснее."
    },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        films[id] = film
        return films[id]
    else:
        abort(404)


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)

    films.append(film)
    new_index = len(films) - 1
    return jsonify({"id": new_index}), 201


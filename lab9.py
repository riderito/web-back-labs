from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)


# Отображение формы для ввода имени
@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:  # Проверка, чтобы имя не было пустым
            error = "Пожалуйста, введите имя"
            return render_template('lab9/index.html', error=error)
        # Перенаправление на страницу ввода возраста с именем пользователя
        return redirect(url_for('lab9.ask_age', username=username))
    return render_template('lab9/index.html')


# Запрос возраста пользователя
@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def ask_age():
    username = request.args.get('username')
    if not username:  # Проверяем, что параметр username передан
        return redirect(url_for('lab9.main'))  # Возврат на начальную страницу
    if request.method == 'POST':
        age = request.form.get('age')
        if not age or not age.isdigit():  # Проверка, что введен корректный возраст
            error = "Пожалуйста, введите корректный возраст"
            return render_template('lab9/age.html', username=username, error=error)
        # Переход к следующему шагу
        return redirect(url_for('lab9.ask_gender', username=username, age=age))
    return render_template('lab9/age.html', username=username)


# Запрос пола пользователя
@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def ask_gender():
    username = request.args.get('username')
    age = request.args.get('age')
    if not username or not age:  # Проверка параметров
        return redirect(url_for('lab9.main'))  # Возврат на начальную страницу
    if request.method == 'POST':
        gender = request.form.get('gender')
        if not gender:
            error = "Пожалуйста, выберите ваш пол"
            return render_template('lab9/gender.html', username=username, age=age, error=error)
        # Переход к следующему шагу с вопросом
        return redirect(url_for('lab9.preferences', username=username, age=age, gender=gender))
    return render_template('lab9/gender.html', username=username, age=age)


# Вопрос о предпочтениях
@lab9.route('/lab9/preferences/', methods=['GET', 'POST'])
def preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if not username or not age or not gender:  # Проверка параметров
        return redirect(url_for('lab9.main'))  # Возврат на начальную страницу
    if request.method == 'POST':
        choice = request.form.get('choice')
        return redirect(url_for('lab9.more_preferences', username=username, age=age, gender=gender, choice=choice))
    return render_template('lab9/preferences.html', username=username, age=age, gender=gender)


@lab9.route('/lab9/more_preferences/', methods=['GET', 'POST'])
def more_preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    choice = request.args.get('choice')  # Что выбрал пользователь ("что-то вкусное" или "что-то красивое")

    if not username or not age or not gender or not choice:
        return redirect(url_for('lab9.main'))

    if request.method == 'POST':
        # Уточнение выбора: сладкое/сытное или природа/искусство
        more_choice = request.form.get('more_choice')

        # Обработка на основе возраста, пола и выбора пользователя
        age = int(age)
        if age < 18:
            age_group = 'child'
        else:
            age_group = 'adult'

        if gender == 'male':
            pronoun = "чудесный мальчик" if age_group == 'child' else "замечательный мужчина"
        else:
            pronoun = "удивительная девочка" if age_group == 'child' else "обворожительная женщина"

        # Формирование поздравления и подбор картинки
        if choice == "что-то вкусное":
            if more_choice == "сладкое":
                gift_image = "candies.jpg"
                wish = "всегда наслаждаться сладкими моментами жизни"
            elif more_choice == "сытное":
                gift_image = "burger.jpg"
                wish = "никогда не быть голодным и наслаждаться вкусной едой"
        elif choice == "что-то красивое":
            if more_choice == "природа":
                gift_image = "nature.jpeg"
                wish = "быть вдохновленным природой каждый день"
            elif more_choice == "искусство":
                gift_image = "art.jpg"
                wish = "всегда находить красоту в искусстве и творчестве"

        congratulation = f"Желаю тебе {wish}. Вот тебе подарок!"
        return render_template('lab9/congratulations.html', username=username, age=age,
            pronoun=pronoun, congratulation=congratulation, gift_image=gift_image)

    # Передаем данные для уточнения выбора
    return render_template('lab9/more_preferences.html', username=username, age=age,
        gender=gender, choice=choice)

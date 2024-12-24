from flask import Blueprint, render_template, request, redirect, url_for, session

lab9 = Blueprint('lab9', __name__)


# Отображение формы для ввода имени
@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    # Если в сессии уже есть данные для поздравления, показываем поздравление
    if 'congratulation' in session:
        return redirect(url_for('lab9.show_congratulation'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:  # Проверка, чтобы имя не было пустым
            error = "Пожалуйста, введите имя"
            return render_template('lab9/index.html', error=error)
        # Сохраняем имя в сессии и переходим на страницу ввода возраста
        session['username'] = username
        return redirect(url_for('lab9.ask_age'))
    return render_template('lab9/index.html')


# Запрос возраста пользователя
@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def ask_age():
    username = session.get('username')
    if not username:  # Проверяем, что имя есть в сессии
        return redirect(url_for('lab9.main'))  # Возврат на начальную страницу
    if request.method == 'POST':
        age = request.form.get('age')
        if not age or not age.isdigit():  # Проверка, что введен корректный возраст
            error = "Пожалуйста, введите корректный возраст"
            return render_template('lab9/age.html', username=username, error=error)
        session['age'] = age  # Сохраняем возраст в сессии
        # Переход к следующему шагу
        return redirect(url_for('lab9.ask_gender'))
    return render_template('lab9/age.html', username=username)


# Запрос пола пользователя
@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def ask_gender():
    username = session.get('username')
    age = session.get('age')
    if not username or not age:
        return redirect(url_for('lab9.main'))
    if request.method == 'POST':
        gender = request.form.get('gender')
        if not gender:
            error = "Пожалуйста, выберите ваш пол"
            return render_template('lab9/gender.html', username=username, age=age, error=error)
        session['gender'] = gender  # Сохраняем пол в сессии
        return redirect(url_for('lab9.preferences'))
    return render_template('lab9/gender.html', username=username, age=age)


# Вопрос о предпочтениях
@lab9.route('/lab9/preferences/', methods=['GET', 'POST'])
def preferences():
    username = session.get('username')
    age = session.get('age')
    gender = session.get('gender')
    if not username or not age or not gender:
        return redirect(url_for('lab9.main'))
    if request.method == 'POST':
        choice = request.form.get('choice')
        session['choice'] = choice  # Сохраняем выбор в сессии
        return redirect(url_for('lab9.more_preferences'))
    return render_template('lab9/preferences.html', username=username, age=age, gender=gender)


@lab9.route('/lab9/more_preferences/', methods=['GET', 'POST'])
def more_preferences():
    username = session.get('username')
    age = session.get('age')
    gender = session.get('gender')
    choice = session.get('choice')

    if not username or not age or not gender or not choice:
        return redirect(url_for('lab9.main'))

    if request.method == 'POST':
        # Уточнение выбора: сладкое/сытное или природа/искусство
        more_choice = request.form.get('more_choice')

        # Обработка на основе возраста, пола и выбора пользователя
        age = int(age)
        age_group = 'child' if age < 18 else 'adult'
        pronoun = ("чудесный мальчик" if age_group == 'child' else "замечательный мужчина") if gender == 'male' else \
                  ("удивительная девочка" if age_group == 'child' else "обворожительная женщина")

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
        
        # Сохраняем поздравление в сессии
        session['congratulation'] = congratulation
        session['gift_image'] = gift_image
        session['pronoun'] = pronoun
        return redirect(url_for('lab9.show_congratulation'))

    # Передаем данные для уточнения выбора
    return render_template('lab9/more_preferences.html', username=username, age=age,
        gender=gender, choice=choice)


# Отображение поздравления
@lab9.route('/lab9/congratulation/')
def show_congratulation():
    if 'congratulation' not in session:
        return redirect(url_for('lab9.main'))
    return render_template(
        'lab9/congratulations.html',
        username=session['username'],
        pronoun=session['pronoun'],
        congratulation=session['congratulation'],
        gift_image=session['gift_image']
    )


# Сброс данных
@lab9.route('/lab9/reset/')
def reset():
    session.clear()
    return redirect(url_for('lab9.main'))

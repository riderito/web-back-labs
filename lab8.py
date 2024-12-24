from flask import Blueprint, render_template, request, redirect, session
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    login = current_user.login if current_user.is_authenticated else 'Anonymous'
    return render_template('lab8/index.html', login=login)


@lab8.route('/lab8/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form:
        return render_template('lab8/register.html',
                               error='Имя пользователя не должно быть пустым')
    
    if not password_form:
        return render_template('lab8/register.html',
                               error='Пароль не должен быть пустым')

    login_exists = users.query.filter_by(login = login_form).first()
    if login_exists:
        return render_template('lab8/register.html',
                               error = 'Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()

    # Автоматический логин после регистрации
    login_user(new_user, remember=False)
    return redirect('/lab8/')


@lab8.route('/lab8/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember_me = request.form.get('remember') == 'on'  # Получаем значение галочки

    if not login_form:
        return render_template('lab8/login.html',
                               error='Имя пользователя не должно быть пустым')
    
    if not password_form:
        return render_template('lab8/login.html',
                               error='Пароль не должен быть пустым')

    user = users.query.filter_by(login = login_form).first()

    if user:
         if check_password_hash(user.password, password_form):
              login_user(user, remember=remember_me)  # Устанавливаем долговременную сессию
              return redirect('/lab8/')
         
    return render_template('/lab8/login.html',
                           error = 'Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/article', methods=['GET', 'POST'])
@login_required
def list_articles():
    status_message = None  # Сообщение о статусе операции

    if request.method == 'POST':
        article_id = request.form.get('article_id')
        is_public = request.form.get('is_public') == 'on'

        article = articles.query.filter_by(id=article_id, user_id=current_user.id).first()
        if article:
            article.is_public = is_public
            db.session.commit()
            status_message = f"Статус статьи «{article.title}» обновлен."
        else:
            status_message = "Ошибка: статья не найдена или недоступна."

    user_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('lab8/list_articles.html', articles=user_articles, status_message=status_message)


@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')


@lab8.route('/lab8/article/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create_article.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = request.form.get('is_public') == 'on'

    if not title or not article_text:
        return render_template('lab8/create_article.html', error = 'Название и текст статьи обязательны!')

    new_article = articles(
        user_id=current_user.id,
        title=title,
        article_text=article_text,
        is_favorite=False,
        is_public=is_public,
        likes=0
    )
    db.session.add(new_article)
    db.session.commit()
    return redirect('/lab8/')


@lab8.route('/lab8/article/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    # Найти статью, принадлежащую текущему пользователю
    article = articles.query.filter_by(id=article_id, user_id=current_user.id).first()

    if not article:
        return redirect('/lab8/article')  # Перенаправить, если статья не найдена

    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')

        if not title or not text:
            return render_template(
                'lab8/edit_article.html',
                article=article,
                error="Название и текст статьи не могут быть пустыми."
            )

        # Обновляем статью
        article.title = title
        article.article_text = text
        db.session.commit()
        return redirect('/lab8/article')

    return render_template('lab8/edit_article.html', article=article)


@lab8.route('/lab8/article/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    # Найти статью, принадлежащую текущему пользователю
    article = articles.query.filter_by(id=article_id, user_id=current_user.id).first()

    if not article:
        return redirect('/lab8/article')  # Перенаправить, если статья не найдена

    # Удалить статью
    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/article')


@lab8.route('/lab8/public')
def public_articles():
    # Получить все публичные статьи
    public_articles = articles.query.filter_by(is_public=True).all()
    return render_template('lab8/public_articles.html', articles=public_articles)


@lab8.route('/lab8/search', methods=['GET', 'POST'])
def search_articles():
    if request.method == 'POST':
        # Получаем строку поиска из формы
        search_query = request.form.get('search_query', '').strip()

        # Если строка пуста, перенаправляем на страницу поиска
        if not search_query:
            return render_template('lab8/search.html', error='Введите строку для поиска.')

        # Получить результаты поиска среди своих и публичных статей
        if current_user.is_authenticated:
            # Ищем свои статьи и публичные статьи других пользователей
            results = articles.query.filter(
                (articles.title.ilike(f'%{search_query}%')) |
                (articles.article_text.ilike(f'%{search_query}%'))
            ).filter(
                (articles.user_id == current_user.id) | (articles.is_public == True)
            ).all()
        else:
            # Для неавторизованных пользователей ищем только среди публичных статей
            results = articles.query.filter(
                (articles.title.ilike(f'%{search_query}%')) |
                (articles.article_text.ilike(f'%{search_query}%'))
            ).filter(articles.is_public == True).all()

        return render_template('lab8/search_results.html', articles=results, query=search_query)

    return render_template('lab8/search.html')


# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/5  8:31
# 文件名称：views.py
# 开发工具：PyCharm

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from watchlist import app, db
from watchlist.models import User, Movie
from sqlalchemy import desc


@app.route('/', methods=['GET', 'POST'])
def index(): 
    # movies = list(Movie.query.order_by('year'))  # 创建一个列表，把所有的电影信息放到列表中,按照年份排序,升序
    # movies = list(Movie.query.order_by(desc(Movie.year)).all())
    # movies = Movie.query.order_by(desc(Movie.year)).all() # 按照观看时间排序,降序    
    # 分页
    page = request.args.get('page', 1, type=int)
    pagination = Movie.query.order_by(desc(Movie.year)).paginate(page, per_page=10, error_out=False)
    movies = pagination.items
    #movies = pagination

    #return render_template('index.html', movies=movies)
    return render_template('index.html', movies=movies, pagination=pagination)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))

        title = request.form['title']
        year = request.form['year']
        cinema_address = request.form['cinema_address']
        cinema_name = request.form['cinema_name']

        if not title or not year or not cinema_address or not cinema_name or len(year) > 10 or len(title) > 128 or len(cinema_address) > 128 or len(cinema_name) > 128:
            flash('Invalid input.')
            return redirect(url_for('index'))

        movie = Movie(title=title, year=year, cinema_address=cinema_address, cinema_name=cinema_name)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))
        
    return render_template('add.html')


@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        cinema_address = request.form['cinema_address']
        cinema_name = request.form['cinema_name']

        if not title or not year or not cinema_address or not cinema_name or len(year) > 10 or len(title) > 128 or len(cinema_address) > 128 or len(cinema_name) > 128:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))

        movie.title = title
        movie.year = year
        movie.cinema_address = cinema_address
        movie.cinema_name = cinema_name
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)


@app.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 128:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        user = User.query.first()
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.')
    return redirect(url_for('index'))

# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/5  8:32
# 文件名称：commands.py
# 开发工具：PyCharm

import click
from watchlist import app, db
from watchlist.models import User, Movie


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
        click.echo('Droped database.')
    else:
        db.create_all()
        click.echo('Initialized database.')


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'Tryrus Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988-01-02', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'King of Comedy', 'year': '1999-02-21', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'Dead Poets Society', 'year': '1989-11-02', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'The Pork of Music', 'year': '2012-05-21', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'A Perfect World', 'year': '1993-12-23', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'WALL-E', 'year': '1999-11-18', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'Leon', 'year': '1993-01-23', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'Mahjong', 'year': '1999-01-02', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'Swallowtail Butterfly', 'year': '1999-01-23', "cinema_address": "china", "cinema_name": "bayicinema"},
        {'title': 'Devils on the Doorstep', 'year': '1999-10-12', "cinema_address": "china", "cinema_name": "bayicinema"},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'], cinema_address=m['cinema_address'], cinema_name=m['cinema_name'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')

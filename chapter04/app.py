# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/4  21:25
# 文件名称：app.py
# 开发工具：PyCharm

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

name = 'Tryrus Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
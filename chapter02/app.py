# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/4  21:25
# 文件名称：app.py
# 开发工具：PyCharm

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return 'Welcome to Tryrus Watchlist!'


@app.route('/home')
def home():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# @app.route('/user/<name>')
# def user_page(name):
#     return 'User page'
#
# from flask import escape
#
# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % escape(name)

from flask import url_for, escape

# # ...
#
# @app.route('/')
# def hello():
#     return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
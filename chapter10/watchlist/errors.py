# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/5  8:31
# 文件名称：errors.py
# 开发工具：PyCharm

from flask import render_template
from watchlist import app


@app.errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

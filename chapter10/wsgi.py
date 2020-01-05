# -*- coding: utf-8 -*-
# 开发人员：Tryrus
# 开发时间：2020/1/5  10:19
# 文件名称：wsgi.py
# 开发工具：PyCharm

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app
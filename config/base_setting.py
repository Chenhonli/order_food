# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "mooc_food"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

# 分页展示配置
PAGE_SIZE = 50
# 显示页数
PAGE_DISPLAY = 10
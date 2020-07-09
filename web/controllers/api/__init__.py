# -*- coding: utf-8 -*-
"""
@Author: chenftli
@Blog: https://blog.csdn.net/Chenftli
@CreateTime: 2020/7/7 17:32
"""
from flask import Blueprint
route_api = Blueprint('api_page', __name__)
from web.controllers.api.Member import *


@route_api.route("/")
def index():
    return "Mini Api V1.0~~"
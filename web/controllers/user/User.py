# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask import template_rendered

route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return template_rendered("user/login.html")
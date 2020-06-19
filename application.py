from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None):
        """
        创建这个类的意义是将不同环境的配置导入到Flask类中，以便实例化app时使用，同时将数据库的orm也直接在初始化app时将db实例化
        :param import_name:
        """
        super(Application, self).__init__(import_name=import_name, template_folder=template_folder)
        self.config.from_pyfile("config/base_setting.py")
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + '/web/templates/')
manager = Manager(app)

"""
函数模板
"""
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.builStaticUrl, 'builStaticUrl')
app.add_template_global(UrlManager.builUrl, 'builUrl')
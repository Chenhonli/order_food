from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name):
        """
        创建这个类的意义是将不同环境的配置导入到Flask类中，以便实例化app时使用，同时将数据库的orm也直接在初始化app时将db实例化
        :param import_name:
        """
        super(Application, self).__init__(import_name)
        self.config.from_pyfile("config/base_setting.py")
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)

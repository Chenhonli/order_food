# order_food
这是一个基于flask的点餐小程序

## 启动
* export ops_config=local|production && python manage.py runserver

## flask-sqlacodegen
    flask-sqlacodegen "mysql://root:123456@127.0.0.1/food_db" --outfile "common/models/models.py" --flask
    flask-sqlacodegen "mysql://root:123456@127.0.0.1/food_db" --tables user --outfile "common/models/user.py" --flask
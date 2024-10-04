from flask import Flask, jsonify, session
from flask_cors import CORS
from autoloading import (
    handlers,
    models
)
from flask_socketio import SocketIO
from .config import *
from threading import Thread

from autoloading.handlers.sensor import(

    read_per_second
)


#线程开启物位计读取
t = Thread(target=read_per_second) 
t.start()

app = Flask(__name__, static_folder='../static', static_url_path='/static', template_folder='../templates')
app.secret_key = SECRET_KEY
# 开启跨域访问
CORS(app, supports_credentials=True)

# 初始化api
handlers.init_app(app=app)



# 创建数据库表
models.init_sqlite(app=app)

# 打印所有路由
with app.app_context():
    print(app.url_map)




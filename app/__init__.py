from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 这个 Config 如果不添加, 用户登录时 flask-login 会报 no secret key 的错误
app.config.from_object(Config)
bootstrap = Bootstrap(app)

login = LoginManager(app)
# 这里是指定 @login_required 标签重定位时的位置
# 根据 routes.py 中的视图函数来进行 login 界面的跳转
login.login_view = 'login_view'

# blueprint for auth part
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# blueprint for errors part
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp, url_prefix='/errors')

from app import routes

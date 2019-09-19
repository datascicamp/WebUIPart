from flask_login import UserMixin
from app import login
from config import Config


class User(UserMixin):

    def __init__(self, account_id):
        # self.username = username
        # uid 是为了 flask-login 记录登录状态
        self.account_id = account_id
        self.account_email = ''
        self.account_nickname = ''

    # 必须写成 get_id 函数名
    def get_id(self):
        return self.account_id

    def get_account_id(self):
        return self.account_id

    def get_account_email(self):
        return self.account_email

    def set_account_email(self, account_email):
        self.account_email = account_email

    def get_account_nickname(self):
        return self.account_nickname

    def set_account_nickname(self, account_nickname):
        self.account_nickname = account_nickname


# 配合 flask-login 进行用户的 session 定位
@login.user_loader
def load_user(account_id):
    user = User(account_id)
    # 返回的类型需要继承 UserMixin 中的4个属性便于 flask-login 利用
    # 详见 https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
    return user

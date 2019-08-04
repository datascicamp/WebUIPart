from flask_login import UserMixin
from app import login


class User(UserMixin):

    def __init__(self, uid):
        # self.username = username
        # uid 是为了 flask-login 记录登录状态
        self.id = uid

    def get_id(self):
        return self.id


# 配合 flask-login 进行用户的 session 定位
@login.user_loader
def load_user(id):
    user = User(id)
    # 返回的类型需要继承 UserMixin 中的4个属性便于 flask-login 利用
    # 详见 https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
    return user

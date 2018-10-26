from blog_app.dao.user_info_dao import UserInfoDao
from blog_app.utils.cryptoutils import CryptoUtil


class LoginService(object):
    def __init__(self):
        self.user_info_dao = UserInfoDao('localhost', 'root', 'root', 'blog_app')

    def login(self, username, password):
        user = self.user_info_dao.find_by_username(username)
        if len(user):
            crypt_password = CryptoUtil.md5_encode(password)
            right_password = crypt_password == user[0][1]
            is_active = user[0][2] == 0
            return right_password and is_active
        else:
            return False





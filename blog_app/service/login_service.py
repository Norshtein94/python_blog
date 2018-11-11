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
            success = right_password and is_active
            if success:
                self.user_info_dao.update_login_time(username)
            return success
        else:
            return False

    def last_login_time(self, username):
        user = self.user_info_dao.find_by_username(username)
        if len(user):
            last_login_time = user[0][3]
            print(last_login_time)
            return last_login_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return ''


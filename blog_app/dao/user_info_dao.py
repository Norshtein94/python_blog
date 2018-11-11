from blog_app.dao.base_dao import BaseDao


class UserInfoDao(BaseDao):
    def find_by_username(self, username):
        sql = "select username,password,status,last_login_time from user_info where username = '%s'" % username
        return super().exec_sql(sql)

    def update_login_time(self, username):
        sql = "update user_info set last_login_time = now() where username = '%s'" % username
        super().exec_sql(sql)


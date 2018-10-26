from blog_app.dao.base_dao import BaseDao


class UserInfoDao(BaseDao):
    def find_by_username(self, username):
        sql = "select username,password,status from user_info where username = '%s'" % username
        return super().exec_sql(sql)

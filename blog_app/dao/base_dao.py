from blog_app.utils.mysqlutils import MysqlUtil


class BaseDao(object):
    def __init__(self, host, user, password, db):
        self.dao = MysqlUtil(host, user, password, db)
        print('init dao %s' % self)

    def __str__(self):
        return 'host:%s,user:%s' % (self.dao.host, self.dao.username)

    def exec_sql(self, sql):
        return self.dao.exec(sql)

import pymysql
import logging

logger = logging.getLogger('test')


class MysqlUtil:
    __host = 'localhost'
    __username = 'root'
    __password = 'root'
    __schema = 'blog_app'
    __port = 3306

    def __init__(self, h, u, p, s, pt):
        self.host = h
        self.username = u
        self.password = p
        self.schema = s
        self.port = pt

    def exec(self, sql):
        logger.info('sql is %s', sql)
        db = pymysql.connect(self.host, self.username, self.password, self.schema, self.port)
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        data = cursor.fetchall()
        logger.debug('data type is %s and data is %s', type(data), data)
        db.close()
        return data


if __name__ == '__main__':
    c = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
    data = c.exec('select now()')
    print(data)

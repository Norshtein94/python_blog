import unittest
import time
import xmlrunner

# Create your tests here.  method should be start with 'test_'
from blog_app.service.login_service import LoginService
from blog_app.utils.cryptoutils import CryptoUtil
from blog_app.utils.mysqlutils import MysqlUtil


class TestFunctions(unittest.TestCase):
    # 每个测试用例执行之前做操作
    def setUp(self):
        print('setUp')

    # 每个测试用例执行之后做操作
    def tearDown(self):
        print('tearDown')

    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(self):
        print('setUpClass')

    def test_mysql(self):
        client = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
        a = client.exec('select 1 from dual')
        self.assertEqual("1", str(a[0][0]))

    def test_mysql2(self):
        client = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
        now = client.exec('select now()')
        self.assertEqual(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), str(now[0][0]))

    def test_user(self):
        client = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
        sql = """ 
                  CREATE TABLE IF NOT EXISTS EMP (
                  ID  INT PRIMARY KEY auto_increment,
                  USERNAME CHAR(20) NOT NULL, 
                  PASSWORD CHAR(100),
                  AGE INT, 
                  SEX CHAR(1), 
                  EMAIL CHAR(50), 
                  ADDRESS CHAR(200) )
                  """
        res = client.exec(sql)
        print(res)
        self.assertIsNotNone(res)

    def test_user_add(self):
        client = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
        password = CryptoUtil.md5_encode('admin')
        insert_sql = "insert into emp values (null, 'admin','" + password + "', 28 , '1' ,'122760@qq.com','上海')"
        res = client.exec(insert_sql)
        self.assertIsNotNone(res)

    def test_user_select(self):
        client = MysqlUtil('localhost', 'root', 'root', 'blog_app', 3306)
        select_sql = "select username,password,status from user_info where username = 'admin'"
        res = client.exec(select_sql)
        print(res)
        for p in res:
            print(p)
            # for col in p:
            #     print(col)
        # self.assertIsNotNone(res)

    def test_login_service(self):
        service = LoginService()
        res = service.login('admin', 'admin')
        print(res)


if __name__ == '__main__':
    # unittest.main()

    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(TestFunctions('test_user_select'))  # 测试套件中添加测试用例
    test_suite.addTest(TestFunctions('test_mysql'))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定报告放的目录
    # 生成执行用例的对象
    runner.run(test_suite)

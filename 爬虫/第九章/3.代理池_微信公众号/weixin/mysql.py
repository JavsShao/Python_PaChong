import pymysql
from weixin.config import *


class MySQL():
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT, database=MYSQL_DATABASE):
        '''
        MySQL初始化
        :param host: 地址
        :param username:用户名
        :param password: 密码
        :param port: 端口号
        :param database: 数据库名称
        '''
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

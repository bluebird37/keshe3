# coding=utf-8
import pymysql
from MysqlSQL import SQL_general

class MysqlOrm:
    def __init__(self):
        self.conn=None
        self.cursor=None

    # 数据库链接信息
    def connect(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='shu1996228+1s',
                port=3306,
                db='project',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor=self.conn.cursor()
            print('mysql access success')
        except:
            print('mysql access error')

    def execute_no_return(self, sql):
        """
        执行SQL语句,不获取返回结果
        :param sql: SQL语句
        """
        try:
            self.cursor.execute(sql)
            print('execute success_nonono')
            return 'true'
        except:
            print('execute error_nonono')
            return 'false'


    def execute(self, sql):
        """
        执行SQL语句
        :param sql: SQL语句
        :return: 获取SQL执行并取回的结果
        """
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print('execute success')
        except:
            print('execute error')
        return result if result else None

    def commit(self):
        self.conn.commit()
        print('commit')

    def close(self):
        self.conn.close()
        print('close')

if __name__=='__main__':
    SQL=SQL_general()
    db=MysqlOrm()
    db.connect()
    input={}
    input['number'] = '1'
    input['password'] = '1'
    input['mail'] = '1'
    input['details'] = '1'
    sql=SQL.teacher_login_search_sql(input)
    result=db.execute(sql)
    if result is not None:
        print("yes")
    else:
        print('no')
    db.commit()
    db.close()
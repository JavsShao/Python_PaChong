import pymysql


# 链接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='970202',db='pachong_test')
# 获取游标
cursor = db.cursor()

# 查询语句
sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    # 计算数据
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    # 查询第一条数据
    print('One:',one)
    result = cursor.fetchall()
except:
    print("出现错误！")
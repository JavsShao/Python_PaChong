import pymysql


# 连接数据库
db = pymysql.connect(host='localhost',port=3306, user='root',password='970202', db = 'pachong_test')
# 获取游标
cursor = db.cursor()
table = 'students'
condition = 'age > 20'

sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
    print("成功")
except:
    print("没有成功")
    db.rollback()

db.close()
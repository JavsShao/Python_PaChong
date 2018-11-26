import pymysql


# 连接数据库
db = pymysql.connect(host='127.0.0.1',user='root',password='970202',db='pachong_test',port=3306)
# 获取游标
cursor = db.cursor()
# 更新数据库
sql = 'update students set age = %s where name = %s'
try:
    cursor.execute(sql, (28,'Bob'))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库
db.close()
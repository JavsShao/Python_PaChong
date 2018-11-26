import pymysql


# 链接
db = pymysql.connect(host='127.0.0.1',user='root',password='970202',port=3306)
# 获取游标
cursor = db.cursor()
# 查询版本
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
try:
    # 创建数据库
    cursor.execute('create database pachong_test charset utf8')
except Exception as e:
    print(e)

db.close()
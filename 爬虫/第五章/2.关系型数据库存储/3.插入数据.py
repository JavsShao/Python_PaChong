import pymysql


id = '20180001'
user = 'Bob'
age = 20

db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='970202',db='pachong_test')
cursor = db.cursor()


# data = {
#     'id':'20180002',
#     'name':'Hamdi',
#     'age':25
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
#
# db.close()

sql = 'insert into students(id, name, age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id, user, age))
    db.commit()
except:
    db.rollback()

db.close()
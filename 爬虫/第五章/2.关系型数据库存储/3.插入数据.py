import pymysql


id = '20180001'
user = 'Bob'
age = 20

db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='970202',db='pachong_test')
cursor = db.cursor()

sql = 'insert into students(id, name, age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id, user, age))
    db.commit()
except:
    db.rollback()

db.close()
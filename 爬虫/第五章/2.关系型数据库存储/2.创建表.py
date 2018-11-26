import pymysql


# 链接
db = pymysql.connect(host='localhost',user='root',password='970202',port=3306,db='pachong_test')
# 获取游标
cursor = db.cursor()
# 创建表
sql = 'create table if not exists students (id varchar (225) not null ,name varchar(225) not null, age int not null ,primary key (id))'
cursor.execute(sql)
db.close()

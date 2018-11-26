import pymysql


# 连接数据库
db = pymysql.connect(host='localhost',user='root',password='970202',port=3306,db='pachong_test')
# 获取游标
cursor = db.cursor()

data = {
    'id':'20180003',
    'name':'zhaowei',
    'age':30
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)

update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update

try:
    if cursor.execute(sql, tuple(data.values()*2)):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()
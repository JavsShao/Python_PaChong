import pymongo


# 连接数据库
client = pymongo.MongoClient(host='127.0.0.1',port=27017)
# 指定数据库
db = client.students_1
# 指定集合(表)
collection = db.students

result = collection.find_one({'name':'Hamdi'})
print(type(result))
print(result)

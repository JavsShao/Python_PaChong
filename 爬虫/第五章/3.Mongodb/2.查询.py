import pymongo


# 连接数据库
client = pymongo.MongoClient(host='127.0.0.1',port=27017)
# 指定数据库
db = client.students_1
# 指定集合(表)
collection = db.students

# result = collection.find_one({'name':'Hamdi'})
# print(type(result))
# print(result)

# result = collection.find({'age':25})
# print(result)
# for resul in result:
#     print(resul)

# 计数
# count = collection.find().count()
# print(count)

# 排序
# results = collection.find().sort('name',pymongo.ASCENDING)
# print([result['name'] for result in results])

# 更新
# condition = {'name':'Hamdi'}
# student = collection.find_one(condition)
# student['name'] = 'zhaowei'
# result = collection.update(condition, student)
# print(result)

# 删除
result = collection.remove({'name':'Hamdi'})
print(result)
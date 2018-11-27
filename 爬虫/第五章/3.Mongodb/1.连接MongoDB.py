import pymongo


client = pymongo.MongoClient(host='localhost',port=27017)
# print('连接成功！')

db = client.students_1

collection = db.students

# 插入数据
student = {
    'id':'20180001',
    'name':'Hamdi',
    'age':25,
    'gender':'male'

}

student2 = {
    'id':'20180002',
    'name':'Mike',
    'age':20,
    'gender':'male'
}

result = collection.insert(student,student2)
print(result)


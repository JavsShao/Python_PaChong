import pymongo


client = pymongo.MongoClient(host='localhost',port=27017)
print('连接成功！')
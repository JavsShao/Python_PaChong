import json


str = '''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1997-02-02"
}, {
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''
data = json.loads(str)
print(data)

# 输出第一个字典
print(data[0])
# 输出第一个字典的姓名
print(data[0]['name'])
print(data[0].get('name'))
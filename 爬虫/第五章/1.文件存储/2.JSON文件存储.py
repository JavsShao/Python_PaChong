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
},{
    "name":"王伟",
    "gender":"男",
    "birthday":"1997-02-02"
}]
'''
data = json.loads(str)
print(data)

# 输出第一个字典
print(data[0])
# 输出第一个字典的姓名
print(data[0]['name'])
print(data[0].get('name'))

# 没有age属性，所以会报错，解决方式是：使用get来获取属性值
# print(data[0]['age'])
print(data[0].get('age'))   # 使用get方法获取属性值，如果没有该属性，那么不会报错，会返回None


print('------输出JSON-----')
# data = [{
#     'name':'Bob',
#     'gender':'male',
#     'birthday':'1992-10-18'
# }]
with open('data.json','w') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))

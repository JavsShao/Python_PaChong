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
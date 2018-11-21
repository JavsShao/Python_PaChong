import requests



data = {
    'name':'Hamdi',
    'age':22
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)


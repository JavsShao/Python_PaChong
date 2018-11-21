from urllib import request, parse


url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0',
    'HOST':'httpbin.org'
}
dict = {
    'name':'Hamdi'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
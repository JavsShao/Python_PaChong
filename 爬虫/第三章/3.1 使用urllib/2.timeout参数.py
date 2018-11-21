import urllib.request


try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.5)
    print(response.read)
except Exception as e:
    print('时间超时，无法请求数据')
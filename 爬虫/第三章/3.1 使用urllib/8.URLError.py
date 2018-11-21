from urllib import request, error


try:
    response = request.urlopen('http://www.baidus.com')
    print(response.read().decode('utf-8'))
except error.URLError as e:
    print(e.reason)
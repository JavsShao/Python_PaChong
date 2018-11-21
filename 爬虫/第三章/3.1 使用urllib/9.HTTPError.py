# from urllib import request, error
#
#
# try:
#     response = request.urlopen('http://www.baidu.com')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# else:
#     print("链接成功！")

import urllib.request,urllib.error
import socket


try:
    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('请求超时！')
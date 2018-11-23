import requests
from pyquery import PyQuery


# doc = PyQuery(url='http://cuiqingcai.com')
# print(doc('title'))

# doc = pq(url='https://www.baidu.com')
# print(doc('title'))

doc = PyQuery(requests.get('http://cuiqingcai.com').text)
print(doc('title'))
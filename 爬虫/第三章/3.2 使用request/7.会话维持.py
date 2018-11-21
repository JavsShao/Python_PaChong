import requests

#
# requests.get('http://httpbin.org/cookies/set/number/12345678')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345678')
r = s.get('http://httpbin.org/cookies')
print(r.text)
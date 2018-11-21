import requests


files = {
    'file':open('favicon.mp3')
}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)
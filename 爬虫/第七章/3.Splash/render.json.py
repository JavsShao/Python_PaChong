import requests


url = 'http://localhost:8050/render.json?url=https://www.taobao.com&html=1'
response = requests.get(url)
print(response.text)
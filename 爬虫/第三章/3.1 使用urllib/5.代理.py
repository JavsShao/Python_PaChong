from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


proxy_handler = ProxyHandler({
    'https':'http://127.0.0.1',
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://httpbin.org')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
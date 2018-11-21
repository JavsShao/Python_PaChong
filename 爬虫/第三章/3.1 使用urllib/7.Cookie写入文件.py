import http.cookiejar, urllib.request


filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)      # 声明一个cookiejar对象
handler = urllib.request.HTTPCookieProcessor(cookie)    # 利用HTTPCOOKIEPRO构建一个handler
opener = urllib.request.build_opener(handler)           # 利用build_opener()方法构建出Opener，
response = opener.open('https://www.baidu.com')         # 执行open()函数
cookie.save(ignore_discard=True, ignore_expires=True)
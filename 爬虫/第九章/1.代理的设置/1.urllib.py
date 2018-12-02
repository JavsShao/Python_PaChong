from urllib import request

url = 'http://httpbin.org/get'

# 代理服务器
proxy_host = 'http-pro.abuyun.com'
proxy_port = '9010'

# 代理隧道验证信息
# 代理隧道验证信息
proxy_user = 'H777PPS5O73S7HVP'
proxy_pass = '110A90014002D130'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host':proxy_host,
    'port':proxy_port,
    'user':proxy_user,
    'pass':proxy_pass,
}
proxy_handler = request.ProxyHandler({
    'http':proxy_meta,
    'https':proxy_meta,
})
opener = request.build_opener(proxy_handler)
try:
    response = opener.open(url)
    print(response.read().decode('utf-8'))
except Exception as e:
    print(e)
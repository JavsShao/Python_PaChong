from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile


# 代理服务器
proxy_host = 'http-pro.abuyun.com'
proxy_port = '9010'

# 代理隧道验证信息
proxy_user = 'H777PPS5O73S7HVP'
proxy_pass = '110A90014002D130'

proxy = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host':proxy_host,
    'port':proxy_port,
    'user':proxy_user,
    'pass':proxy_pass,
}

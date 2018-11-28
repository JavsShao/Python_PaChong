import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(2)
browser.forward()
browser.close()
'''
back():返回上一页
forward():去下一页
'''
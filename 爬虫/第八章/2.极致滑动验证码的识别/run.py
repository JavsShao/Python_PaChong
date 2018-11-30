from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# 配置
EMAIL = 'javs_shao@163.com'
PASSWORD = 'QWERTY1234'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait
        self.emaile = EMAIL
        self.password = PASSWORD
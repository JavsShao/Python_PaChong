from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = 'Hamdi__'
PASSWORD = 'QWERTY0202'

TEMPLATES_FOLDER = 'templates'

class CrackWeiboSlide():
    def __init__(self):
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from .captach import Chaojiying

Email = 'javs_shao@163.com'
PASSWORD = '111'

CHAOJIYING_USERNAME = 'Hamdi0202'
CHAOJIYING_PASSWORD = 'qwerty1234'
CHAOJIYING_SOFT_ID = 897939
CHAOJIYING_KIND = 2002


class CrackTouClick(object):

    def __init__(self):
        '''
        初始化
        '''
        self.url = 'http:admin.touclick.com/login.html'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = Email
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD,CHAOJIYING_SOFT_ID)

    def __del__(self):
        '''
        关闭浏览器
        :return:
        '''
        self.browser.close()
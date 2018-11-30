from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .captach import Chaojiying
from selenium.webdriver.support import expected_conditions as EC

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

    def open(self):
        '''
        打开网页输入用户名和密码（填写表单）
        :return:
        '''
        self.browser(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        email.send_keys(self.password)

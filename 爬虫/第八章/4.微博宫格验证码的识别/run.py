from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'Hamdi__'
PASSWORD = 'QWERTY0202'

TEMPLATES_FOLDER = 'templates'

class CrackWeiboSlide():
    def __init__(self):
        '''
        初始化
        '''
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD

    def __del__(self):
        '''
        关闭浏览器
        :return:
        '''
        self.browser.close()

    def open(self):
        '''
        打开网页输入用户名密码并点击
        :return:
        '''
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(((EC.presence_of_element_located((By.ID, 'loginPassword')))))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

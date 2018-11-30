from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 配置
EMAIL = 'javs_shao@163.com'
PASSWORD = 'QWERTY1234'

class CrackGeetest():
    def __init__(self):
        '''
        初始化
        '''
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait
        self.emaile = EMAIL
        self.password = PASSWORD

    def __del__(self):
        '''
        关闭浏览器
        :return:
        '''
        self.browser.close()

    def get_geetest_button(self):
        '''
        获取初始验证按钮
        :return:验证对象
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.get_geetest_button()
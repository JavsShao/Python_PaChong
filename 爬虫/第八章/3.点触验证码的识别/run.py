import time
from io import BytesIO

from PIL import Image
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

    def get_touclick_button(self):
        '''
        获取初始验证按钮
        :return:
        '''
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-hod-wrap')))
        return button

    def get_touclick_element(self):
        '''
        获取验证码图片对象
        :return: 图片对象
        '''
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-pub-content')))
        return element

    def get_screenshot(self):
        '''
        获取网页截图
        :return:
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name='captcha.png'):
        '''
        获取验证码图片
        :param name:
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_position()
        print('验证码位置：',top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop(left, top, right, bottom)
        captcha.save(name)
        return captcha

    def get_position(self):
        '''
        获取验证码位置
        :return: 验证码位置元组
        '''
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return {top, bottom, left, right}

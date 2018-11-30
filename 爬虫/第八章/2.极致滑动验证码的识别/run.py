import time
from io import BytesIO

from PIL import Image
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

    def get_possition(self):
        '''
        获取验证码的位置
        :return:
        '''
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'], + size['height'], location['width']
        return (top, bottom, left, right)

    def get_screenhot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_geetest_image(self, name='captcha.png'):
        '''
        获取验证码图片
        :param name:
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_possition()
        print('验证码位置，',top, bottom,left, right)
        screenshot = self.get_screenhot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save()
        return captcha

    def open(self):
        '''
        打开网页：输入用户名和密码
        :return:
        '''
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_rap(self, image_1, image_2):
        '''
        获取缺口偏移量
        :param image_1: 不带缺口图片
        :param image_2: 带缺口图片
        :return:
        '''
        left = 60
        for i in range(left, image_1.size[0]):
            for j in range(image_2.size[0]):
                if not self.is_pixel_equal(image_1, image_2, i, j):
                    left = i
                    return left
            return left

    def is_pixel_equal(self, image_1, image_2, x, y):
        '''
        判断两个像素是否相同
        :param image_1: 图片1
        :param image_2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        '''
        # 取两个图片的像素点
        pixel_1 = image_1.load()[x, y]
        pixel_2 = image_2.load()[x, y]
        threshold = 60
        if abs(pixel_1[0] - pixel_2[0]) < threshold and abs(pixel_1[1] - pixel_2[1]) < threshold and abs(
                pixel_1[2] - pixel_2[2]) < threshold:
            return True
        else:
            return False

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track


if __name__ == '__main__':
    crack = CrackGeetest()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

broswer = webdriver.Chrome()
wait = WebDriverWait(broswer,10)
def get_url():
    #网址可以更改为用微博登录的网址'https://weibo.com/login.php?spm=a2107.1.0.0.337911d9Xjeo8U&entry=taobao&goto=https%3A%2F%2Flogin.taobao.com%2Faso%2Ftvs%3Fdomain%3Dweibo%26sid%3De14b81726a49329b0db026af4eff8357%26target%3D68747470733A2F2F7777772E7461'
    url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9l2Cj72&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    #您已经将网址更改微博登录网址可以省略这步直接用输入用户名密码阶段。
    broswer.get(url)
    button_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
    button_login.click()
    time.sleep(2)
    button_login1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_OtherLogin > a.weibo-login')))
    button_login1.click()


    EMAIL = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(2) > div > input')))

    EMAIL.send_keys('chifengshaolei@sina.cn')
    PASSWD = wait.until((EC.presence_of_element_located((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(3) > div > input'))))
    PASSWD.send_keys('QWERTY0202')
    time.sleep(3)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span')))
    button.click()

if __name__ == '__main__':
    get_url()

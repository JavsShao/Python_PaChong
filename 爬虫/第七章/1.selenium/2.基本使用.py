from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


brower = webdriver.Chrome()
try:
    brower.get('https://www.baidu.com')
    input = brower.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(brower, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # 浏览器当前访问的网址(url)
    # print(brower.current_url)
    # 获取当前访问的cookies
    # print(brower.get_cookies())
    # 输入源码
    # print(brower.page_source)
finally:
    # 关闭浏览器
    brower.close()
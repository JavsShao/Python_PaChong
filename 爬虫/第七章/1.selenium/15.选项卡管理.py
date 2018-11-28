import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 开启新的选项卡
browser.execute_script('window.open()')
# 调用weindow_handles属性获取当前开启的所有选项卡，返回的是选项卡的代号列表
print(browser.window_handles)
# 切换选项卡
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(3)
# 切换选项卡
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.tencent.com')
time.sleep(5)
browser.close()
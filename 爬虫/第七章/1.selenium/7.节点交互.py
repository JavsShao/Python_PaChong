from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')

# 因为淘宝网的搜索按钮下的div只有这一个功能，所以btn-search 和 search-button功能一样，但是规范用起来应该是btn-search0p
button = browser.find_element_by_class_name('btn-search')
# button = browser.find_element_by_class_name('search-button')
button.click()
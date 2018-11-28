from selenium import webdriver
from selenium.webdriver import ActionChains

# 获取属性
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
#
# print('-----分隔符------')
# logo = browser.find_element_by_class_name('zu-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本值
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# input = browser.find_element_by_class_name('hide-text')
# print(input.text)

# 获取id，位置，标签名和大小
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
# id属性
print(input.id)
# 相对位置
print(input.location)
# 获取标签名称
print(input.tag_name)
# 节点大小
print(input.size)
browser.close()
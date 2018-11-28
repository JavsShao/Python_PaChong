from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
print(input_first)

input_second = browser.find_element_by_css_selector('#q')
print(input_second)

input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_third)

browser.close()
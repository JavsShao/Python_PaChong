from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote


# 声明浏览器对象
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# 要搜索的商品
KEYWORD = 'iPad'


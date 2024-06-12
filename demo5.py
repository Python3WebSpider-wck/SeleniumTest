from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# input = browser.find_element_by_id('q')
# input = browser.find_element(By.ID, 'q')
input = browser.find_element(By.CSS_SELECTOR, '.rax-view.searchbar-input-wrap')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button = browser.find_element(By.CLASS_NAME, 'btn-search')
# <span class="rax-text-v2 search-button-text">搜索</span>
# button = browser.find_element(By.CLASS_NAME, '.rax-text-v2.search-button-text')
# button.click()

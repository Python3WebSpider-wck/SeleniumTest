from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# # browser.find_element_by_id('hello')
# browser.find_element(By.ID, 'hello')

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element(By.ID, 'hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# print(browser.page_source)

# input_first = browser.find_element_by_id('q')
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)

# input_second = browser.find_element_by_css_selector('#q')
# input_second = browser.find_element(By.CSS_SELECTOR, '#q')
# print(input_second)

# input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
print(input_third)

# print(input_first, input_second, input_third)
browser.close()

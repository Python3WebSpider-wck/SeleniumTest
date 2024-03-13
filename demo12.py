from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://spa2.scrape.center/')
# input = browser.find_element_by_class_name('logo-image')
input = browser.find_element(By.CLASS_NAME, 'logo-image')
print(input)

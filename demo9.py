from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# url = 'https://dynamic2.scrape.cuiqingcai.com/'
url = 'https://spa2.scrape.center/'
browser.get(url)
# input = browser.find_element_by_class_name('logo-title')
input = browser.find_element(By.CLASS_NAME, 'logo-title')
print(input.text)

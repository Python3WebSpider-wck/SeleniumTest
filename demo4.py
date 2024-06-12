from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.rax-view.category-list')
# lis = browser.find_elements(By.CSS_SELECTOR, '.category-list')
lis = browser.find_elements(By.CSS_SELECTOR, '.first-category-wrap')
print(f"len(lis) = {len(lis)}")
print(lis)
browser.close()



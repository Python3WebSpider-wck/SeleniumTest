from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    # 以下代码报错：AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'
    # 原因：webdriver.Chrome() 返回的是 WebDriver 对象而不是 WebElement 对象，
    # 因此无法直接使用 find_element_by_id() 方法。
    # input = browser.find_element_by_id('kw')
    input = browser.find_element(By.ID, 'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

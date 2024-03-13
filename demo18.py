import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

use_script = True
if use_script:
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=option)
    browser.execute_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    browser.get('https://antispider1.scrape.center/')
    time.sleep(5)
    browser.close()
else:
    browser = webdriver.Chrome()
    browser.get('https://antispider1.scrape.center/')
    time.sleep(5)
    browser.close()

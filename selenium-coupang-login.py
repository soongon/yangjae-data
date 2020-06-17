from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://login.coupang.com/login/login.pang')
driver.find_element_by_name('email').send_keys('soongon@gmail.com')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_css_selector('body > div.member-wrapper.member-wrapper--flex > div > div > form > div.login__content.login__content--trigger > button')\
    .click()

time.sleep(3)

driver.close()
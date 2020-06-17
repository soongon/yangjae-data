from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')

# 사용...
time.sleep(5)
driver.get('https://www.coupang.com/np/campaigns/82/components/194176?page=1')

soup = BeautifulSoup(driver.page_source, 'html.parser')

time.sleep(3)

driver.close()
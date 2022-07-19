from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Repos/behaveTestExample/drivers/chromedriver.exe')

driver.get('http://automationpractice.com/')
time.sleep(1)

# common functions
def click_element_by_css_selector(selector) :
    driver.find_element(By.CSS_SELECTOR, selector).click()

# page object de login
LOGIN_BUTTON = '.login'
SUBMIT_LOGIN_BUTTON = '#SubmitLogin'


# step definition de login
click_element_by_css_selector(LOGIN_BUTTON)
driver.find_element(By.CSS_SELECTOR, '#email').is_displayed()
driver.find_element(By.CSS_SELECTOR, '#email').send_keys('n@b.com')

driver.find_element(By.CSS_SELECTOR, '#passwd').send_keys('123456')
click_element_by_css_selector(SUBMIT_LOGIN_BUTTON)

assert driver.find_element(By.CSS_SELECTOR, '.logout').is_displayed()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#Utils/driver.py
driver=webdriver.Chrome('C:/Repos/behaveTestExample/drivers/chromedriver.exe')

def click_element_by_css_selector(selector) :
    driver.find_element(By.CSS_SELECTOR, selector).click()

def go_to_website(url) :
    driver.get(url)

def fill_any_field(selector, texto) :
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(texto)

#Constantes SIEMPRE EN MAYUSCULAS - login.page
HOME_PAGE='http://automationpractice.com/index.php'
LOGIN_BUTTON='.login'
FIELD_EMAIL='#email'
FIELD_PASSWD='#passwd'
SUBMIT_BUTTON='#SubmitLogin'

#Steps/login_steps.py
go_to_website(HOME_PAGE)

time.sleep(1)
click_element_by_css_selector(LOGIN_BUTTON)
fill_any_field(FIELD_EMAIL , 'maxil4d@gmail.com')
fill_any_field(FIELD_PASSWD , 'ABC1234+')

click_element_by_css_selector(SUBMIT_BUTTON)





email_field = driver.find_element(By.CSS_SELECTOR, '#email')
email_field.send_keys('maxil4d@gmail.com')
password_field = driver.find_element(By.CSS_SELECTOR, '#email')
password_field.send_keys('ABC1234+')

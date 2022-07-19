from cgitb import text
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
##from selenium.webdriver.common.keys import Keys

#utils/driver.py
driver = webdriver.Chrome('../drivers/chromedriver.exe')
##driver.get('https://www.google.com')
##print(driver.title)

## precond tener un usuario registrado n@b.com pass: 123456
##1 navegar a http://automationpractice.com/index.php
#Driver.py
#driver.get('http://automationpractice.com/index.php')

def click_element_by_css_selector(selector) :
    driver.find_element(By.CSS_SELECTOR, selector).click()

def go_to_website(url) :
    driver.get(url)

def complet_field(selector,text) :
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(text)

#page_objects/login_page.py
HOME_PAGE = 'http://automationpractice.com/index.php'
LOGIN_BTN = ".login"
EMAIL_FIELD = "#email"
PASSWORD_FIELD = "#passwd"
SUBMIT_BTN = "#SubmitLogin"
EMAIL = "n@b.com"
PASSWORD = "123456"

#steps/login_steps.py
go_to_website(HOME_PAGE)
time.sleep(1)
click_element_by_css_selector(LOGIN_BTN)
complet_field(EMAIL_FIELD,EMAIL)
complet_field(PASSWORD_FIELD,PASSWORD)
click_element_by_css_selector(SUBMIT_BTN)

##2 hacer click boton "sign in" 
#time.sleep(5)
#driver.find_element(By.CSS_SELECTOR, ".login").click()
##3 completar campo "Email address"
##driver.find_element(By.XPATH, "//*[@id='email']")
##driver.find_element(By.CSS_SELECTOR, ".login").click()
##time.sleep(5)
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("n@b.com")
##email_field.send_keys("n@b.com")
##4 completar campo "Password"
##password_field = driver.find_element(By.CSS_SELECTOR, "#passwd")
##password_field.send_keys("123456")
##5 hacer click en el boton "Sign in"
##6 se ve boton con el nombre 
 


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
##from selenium.webdriver.common.keys import Keys

#utils/common_constants.py

driver=webdriver.Chrome('../drivers/chromedriver.exe')

def click_element_by_css_selector(selector) :
   driver.find_element(By.CSS_SELECTOR, selector ).click()

def go_to_website(URL) :
    driver.get (URL)

def llenar_campo (selector,texto) :
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(texto)

#login.page
HOME_PAGE = 'http://automationpractice.com/index.php'
LOGIN_BUTTON = '.login' 
CAMPO_EMAIL = "#email"
CAMPO_PASS = "#passwd"
SUBMIT_BUTTON = '#SubmitLogin'
EMAIL = "elenano10_12@gmail.com"
PASS = "exa46856"
#step definition-login
go_to_website(HOME_PAGE)
##driver.get('https://www.google.com')
##print(driver.title)

##precond tener un usuario registrado elenano10_12@hotmail.com pass: exa46856
##1 navegar a http://automationpractice.com/index.php

##2 hacer click boton 'sing in'
time.sleep(1)

click_element_by_css_selector(LOGIN_BUTTON)
##3 completar campo "email adress"
llenar_campo(CAMPO_EMAIL, EMAIL)
##4 completar campo "password"
llenar_campo(CAMPO_PASS, PASS)
##5 hacer click en boton sing in 
click_element_by_css_selector( SUBMIT_BUTTON )
##6 se ve boton con el nombre

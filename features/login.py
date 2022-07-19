from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
#utils/driver.py
driver = webdriver.Chrome('c:/repo/behaveTestExample/drivers/chromedriver.exe')

def click_element_by_css_selector(selector) :
    driver.find_element(By.CSS_SELECTOR, selector ).click()

def go_to_website(url) :
    driver.get(url)

def llenar_campo(selector,texto) :
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(texto)
#page_objects/login_page.py
HOME_PAGE='http://automationpractice.com/index.php'
LOGIN_BUTTON=".login"
CAMPO_EMAIL="#email"
CAMPO_PASSWD="#passwd"
BUTTON_SUBMITLOGIN="#SubmitLogin"
#steps/login_steps.py
go_to_website(HOME_PAGE)


time.sleep(1)
click_element_by_css_selector(LOGIN_BUTTON)
llenar_campo(CAMPO_EMAIL,"rikioliva@hotmail.com")
llenar_campo(CAMPO_PASSWD,"123456")
#SubmitLogin
click_element_by_css_selector(BUTTON_SUBMITLOGIN)
#hola mundo
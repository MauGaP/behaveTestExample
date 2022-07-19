from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


##Agregado por mi
from selenium.webdriver.chrome.service import Service


from page_objects.LoginPage import HOME_PAGE,LOGIN_BUTTON,CAMPO_EMAIL,CAMPO_PASSWORD,BUTTON_SUBMIT
from utils.Driver import go_to_website,llenar_campo,click_element_by_css_selector,click_element_by_id_selector

#Importados por mi#
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from features.page_objects.BasePage import locate_element_by_css_selector

#utils/driver.py, aca itria esta parte, def es para definir funciones que se utilizan mas abajo
#driver = webdriver.Chrome(executable_path= r'C:/Repos/behaveTestExample/drivers/chromedriver.exe')

#def click_element_by_css_selector(selector):
#   driver.find_element(By.CSS_SELECTOR,selector).click()

## Precondicion: crearse un usuario, User: laural@gmail.com, password:123456
#def define FUNCIONES que se usan mas abajo
#def go_to_website(url):
#    driver.get(url)

#def llenar_campo(selector,texto):
#    driver.find_element(By.CSS_SELECTOR,selector).send_keys(texto)

#page_object/login_page.py, aca se definen las CONSTANTES, que se usan en las llamadas a FUNCIONES
#HOME_PAGE="http://automationpractice.com/index.php"
#LOGIN_BUTTON=".login"
#CAMPO_EMAIL="laural@gmail.com"
#CAMPO_PASSWORD="123456"
#BUTTON_SUBMIT="SubmitLogin"

#steps/login_steps.py definitos-login
go_to_website(HOME_PAGE) 


time.sleep(1)

## Hacer click en el boton sign in 
##driver.find_element(By.CSS_SELECTOR,'.login').click

##Agregado por mi##
#wait = WebDriverWait(driver, 10)
time.sleep(1)
#driver.find_element(By.CSS_SELECTOR,'.login').click
click_element_by_css_selector(LOGIN_BUTTON)

#sigIn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".login")))
#igIn.click()


## Llenar el email y password
#email=wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR,'#email')))
#email.send_keys('laural@gmail.com')
#driver.find_element(By.CSS_SELECTOR,'#email').is_displayed()
#driver.find_element(By.CSS_SELECTOR,'#email').send_keys('laural@gmail.com')
time.sleep(3)

llenar_campo('#email',CAMPO_EMAIL)

#driver.find_element(By.CSS_SELECTOR,'#passwd').is_displayed()
#driver.find_element(By.CSS_SELECTOR,'#passwd').send_keys('123456')

llenar_campo('#passwd',CAMPO_PASSWORD)


# Hacer click en el boton "sign in"
click_element_by_id_selector(BUTTON_SUBMIT)

# Validar que se pudo loguear, chequeando que se muestre el boton desloguear
assert driver.find_element(By.CSS_SELECTOR(".logout").is_displayed())


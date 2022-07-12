from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

##Agregado por mi
from selenium.webdriver.chrome.service import Service

#Importados por mi#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path= r'C:/Repos/behaveTestExample/drivers/chromedriver.exe')


## Precondicion: crearse un usuario, User: laural@gmail.com, password:123456
## navegar a http://automationpractice.com/index.php

driver.get("http://automationpractice.com/index.php")


## Hacer click en el boton sign in 
##driver.find_element(By.CSS_SELECTOR,'.login').click

##Agregado por mi##
wait = WebDriverWait(driver, 10)
time.sleep(1)
#driver.find_element(By.CSS_SELECTOR,'.login').click

sigIn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".login")))
sigIn.click()


## Llenar el email y password
#email=wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR,'#email')))
#email.send_keys('laural@gmail.com')
driver.find_element(By.CSS_SELECTOR,'#email').is_displayed()
driver.find_element(By.CSS_SELECTOR,'#email').send_keys('laural@gmail.com')

driver.find_element(By.CSS_SELECTOR,'#passwd').is_displayed()
driver.find_element(By.CSS_SELECTOR,'#passwd').send_keys('123456')
#time.sleep(1)
#driver.find_element(By.CSS_SELECTOR,'.login').click

# Hacer click en el boton "sign in"
driver.find_element(By.ID,"SubmitLogin").click()

# Validar que se pudo loguear, chequeando que se muestre el boton desloguear

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

## from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Repos/behaveTestExample/drivers/chromedriver.exe')
## driver.get ('https://google.com')
## print(driver.title)

## ir a http://automationpractice.com/index.php
driver.get('http://automationpractice.com/index.php')
## hacer click en boton Sing In (inspeccionar, buscar selector, copiar selector)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.login').click()
## completar campo Email address    mikmik@gmail.com   
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("mikmik@gmail.com")
## completar campo Password   MIKMIK
driver.find_element(By.CSS_SELECTOR, "#passwd").send_keys("MIKMIK")
##Click en loguear
driver.find_element(By.CSS_SELECTOR, '#SubmitLogin').click()
## validar elemento en lapagina sing out
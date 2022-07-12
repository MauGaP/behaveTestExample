from selenium import webdriver
import time
from selenium.webdriver.common.by import By
##from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../drivers/chromedriver.exe')
##driver.get('https://www.google.com')
##print(driver.title)

## precond tener un usuario registrado n@b.com pass: 123456
##1 navegar a http://automationpractice.com/index.php
driver.get('http://automationpractice.com/index.php')
##2 hacer click boton "sign in" 
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".login").click()
##3 completar campo "Email address"
##driver.find_element(By.XPATH, "//*[@id='email']")
time.sleep(5)
##driver.find_element(By.CSS_SELECTOR, ".login").click()
##time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("n@b.com")
##email_field.send_keys("n@b.com")
##4 completar campo "Password"
##password_field = driver.find_element(By.CSS_SELECTOR, "#passwd")
##password_field.send_keys("123456")
##5 hacer click en el boton "Sign in"
##6 se ve boton con el nombre 
 


import os

from selenium import webdriver

#Agregado por mi
from selenium.webdriver.common.by import By



def launch_browser(context, browser):
    cwd = os.getcwd()
    if browser == "firefox":
        context.driver = webdriver.Firefox(executable_path=cwd + '\drivers\geckodriver.exe')
        context.driver.implicitly_wait(10)
    else:
        context.driver = webdriver.Chrome(executable_path=cwd + '\drivers\chromedriver.exe')
        context.driver.implicitly_wait(10)


def navigate_to_url(context, url):
    context.driver.get(url)

##Agregado por mi, utils/driver.py, aca itria esta parte, def es para definir funciones que se utilizan mas abajo
driver = webdriver.Chrome(executable_path= r'C:/Repos/behaveTestExample/drivers/chromedriver.exe')

## Precondicion: crearse un usuario, User: laural@gmail.com, password:123456
#def define FUNCIONES que se usan mas abajo
def go_to_website(url):
    driver.get(url)

def click_element_by_css_selector(selector):
   driver.find_element(By.CSS_SELECTOR,selector).click()

#Agregado
def click_element_by_id_selector(selector):
   driver.find_element(By.ID,selector).click()

def llenar_campo(selector,texto):
    driver.find_element(By.CSS_SELECTOR,selector).send_keys(texto)


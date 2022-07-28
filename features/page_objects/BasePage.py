from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)


def wait_until_element_displayed(self, locator):
    WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(locator))


def wait_until_url_changes(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.url_changes)
<<<<<<< HEAD


def wait_until_alert_is_present(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.alert_is_present())

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome('C:/Repos/behaveTestExample/drivers/chromedriver.exe')

def click_elemrnt_by_css_selector(selector) :
    driver.find_element(By.CSS_SELECTOR, selector).click()

def go_to_website(url) :
    driver.get(url)

def llenar_campo(selector, string) :
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(string)
=======
>>>>>>> 0dcbc8f40d049594056217fe0b41570675bb96e9

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()

def get_element_text(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).text


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)


def wait_until_element_displayed(self, locator):
    WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(locator))


def wait_until_url_changes(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.url_changes)

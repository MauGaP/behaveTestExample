from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element_by_css_selector(css_selector).click()


def click_element_by_id(self, id):
    self.driver.find_element_by_id(id).click()


def locate_element_by_css_selector(self, css_selector):
    element = self.driver.find_element_by_css_selector(css_selector)
    return element


def locate_element_by_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element


def locate_elements_by_class(self, class_name):
    elements = self.driver.find_elements_by_class_name(class_name)
    return elements


def locate_elements_by_css_selector(self, css_selector):
    return self.driver.find_elements_by_css_selector(css_selector)


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element_by_css_selector(css_selector).send_keys(text)


def send_keys_by_id(self, id, text):
    self.driver.find_element_by_id(id).send_keys(text)


def validate_alert_message(self, text_message):
    try:
        wait_until_alert_is_present(self)
        alert = self.driver.switch_to.alert
        if text_message == alert.text:
            alert.accept()
            return True
        else:
            alert.accept()
            return False

    except TimeoutException:
        print("no alert")


def wait_until_element_displayed(self, locator):
    WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(locator))


def wait_until_url_changes(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.url_changes)


def wait_until_alert_is_present(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.alert_is_present())

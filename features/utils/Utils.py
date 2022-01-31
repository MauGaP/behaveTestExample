from selenium import webdriver


def click_element_by_id(self, id):
    self.driver.find_element_by_id(id).click()


def send_keys_by_id(self, id, text):
    self.driver.find_element_by_id(id).send_keys(text)


def click_element_by_css(self, css_selector):
    self.driver.find_element_by_css_selector(css_selector).click()


def send_keys_by_css(self, css_selector, text):
    self.driver.find_element_by_css_selector(css_selector).send_keys(text)


def find_element_by_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element

from selenium import webdriver


def click_element_by_id(context, id):
    context.driver.find_element_by_id(id).click()


def send_keys_by_id(context, id, text):
    context.driver.find_element_by_id(id).send_keys(text)


def click_element_by_css(self, cssSelector):
    self.driver.find_element_by_css_selector(cssSelector).click()

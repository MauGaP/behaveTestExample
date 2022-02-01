def click_element_by_css(self, css_selector):
    self.driver.find_element_by_css_selector(css_selector).click()


def click_element_by_id(self, id):
    self.driver.find_element_by_id(id).click()


def locate_element_by_css(self, css_selector):
    element = self.driver.find_element_by_css_selector(css_selector)
    return element


def locate_element_by_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element


def locate_elements_by_class(self, class_name):
    elements = self.driver.find_elements_by_class_name(class_name)
    return elements


def send_keys_by_css(self, css_selector, text):
    self.driver.find_element_by_css_selector(css_selector).send_keys(text)


def send_keys_by_id(self, id, text):
    self.driver.find_element_by_id(id).send_keys(text)

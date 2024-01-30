from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class base_page:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_web_elements(self, web_elements, locator):
        return web_elements.find_elements(*locator)

    def write_text(self, locator, text):
        web_elem = self.driver.find_element(*locator)
        web_elem.send_keys(text)

    def click_on(self, locator):
        self.wait_clickable_element(locator)
        self.get_element(locator).click()

    def wait_visible_element(self, locator, timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return element.is_displayed()

    def wait_clickable_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return element.is_displayed()

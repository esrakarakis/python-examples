from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_element(self, selector):
        return self.wait.until(EC.element_to_be_clickable(selector))

    def visible_elements(self, selector):
        return self.wait.until(EC.presence_of_all_elements_located(selector))

    def exist_element(self, selector):
        try:
            self.wait.until(EC.presence_of_element_located(selector))
            return True
        except TimeoutException:
            return False

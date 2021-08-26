from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class CategoryPage:
    PAGE_NUMBERS = (By.CSS_SELECTOR, '.a-normal')
    GO_TO_PRODUCT = (By.CSS_SELECTOR, '.s-image')
    IS_SECOND_CATEGORY_PAGE = (By.CSS_SELECTOR, '.a-selected')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def second_page(self):
        self.methods.visible_elements(
            self.PAGE_NUMBERS)[0].click()
        assert self.methods.wait_element(
            self.IS_SECOND_CATEGORY_PAGE).text, "2"

    def click_product(self):
        self.methods.visible_elements(self.GO_TO_PRODUCT)[2].click()

from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class CategoryPage:
    NEXT_BUTTON = (By.CSS_SELECTOR, '.a-pagination > .a-last')
    GO_TO_PRODUCT = (By.CSS_SELECTOR, '.s-image')
    IS_SECOND_CATEGORY_PAGE = (By.CSS_SELECTOR, '.a-selected')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def second_page(self):
        self.methods.visible_elements(
            self.NEXT_BUTTON).click()
        assert self.methods.wait_element(
            self.IS_SECOND_CATEGORY_PAGE).text, "2"

    def click_product(self):
        self.methods.visible_elements(self.GO_TO_PRODUCT)[2].click()

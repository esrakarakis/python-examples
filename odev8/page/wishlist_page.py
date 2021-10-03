from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class WishlistPage:

    DELETE_ITEM = (By.NAME, 'submit.deleteItem')
    IS_PRODUCT_DELETED = (By.CSS_SELECTOR, '.a-alert-inline-success')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def delete_item(self):
        self.methods.wait_element(self.DELETE_ITEM).click()
        assert self.methods.exist_element(
            self.IS_PRODUCT_DELETED), "ürün silindi"

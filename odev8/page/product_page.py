from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class ProductPage:

    ADD_TO_LIST = (By.ID, 'wishListMainButton')
    VIEW_YOUR_LIST = (By.ID, '.wishlistButtonStack')
    PRODUCT_NAME = (By.ID, '.titleSection')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def add_product_to_list(self):
        self.methods.wait_element(self.ADD_TO_LIST).click()
        assert self.methods.wait_element(
            self.PRODUCT_NAME).is_displayed(), "Ürün Bulundu"

    def go_to_wishlist(self):
        self.methods.wait_element(self.VIEW_YOUR_LIST).click()

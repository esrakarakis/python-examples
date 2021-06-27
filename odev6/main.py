from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LCW:
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".dropdown-toggle")
    IS_CATEGORY_PAGE = (By.CSS_SELECTOR, ".product-item-wrapper")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".a_model_item")
    SELECT_SIZE = (By.CSS_SELECTOR, ".option-size a:nth-child(6)")
    SELECTED_SIZE = (By.CSS_SELECTOR, "a.selected")
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart")
    ADDED_TO_CART = (By.CSS_SELECTOR, ".header-cart-quantity")
    CART_PAGE = (By.CSS_SELECTOR, ".bndl-shopping-bag-dims")
    IS_CART_PAGE = (By.CSS_SELECTOR, ".products-area")
    HOME_PAGE = (By.CSS_SELECTOR, ".img-logo")
    IS_HOME_PAGE = (By.CSS_SELECTOR, ".home-main-banner-area")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.website = "https://www.lcwaikiki.com/tr-TR/TR"
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 30)

    def test_navigate(self):
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[3].click()
        assert len(self.wait.until(ec.presence_of_all_elements_located(self.IS_CATEGORY_PAGE))) > 10, True

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()
        assert "SEPETE EKLE" in self.driver.page_source

        self.wait.until(ec.presence_of_all_elements_located(self.SELECT_SIZE))[0].click()
        assert self.wait.until(ec.presence_of_element_located(self.SELECTED_SIZE)).is_displayed, True

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        assert self.wait.until(ec.presence_of_element_located(self.ADDED_TO_CART)).is_displayed, True

        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(self.IS_CART_PAGE)).is_displayed, True

        self.wait.until(ec.element_to_be_clickable(self.HOME_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(self.IS_HOME_PAGE)).is_displayed, True

        self.driver.quit()


LCW().test_navigate()

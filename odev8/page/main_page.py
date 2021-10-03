from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class MainPage:

    WEBSITE = ('https://www.amazon.com')
    SEARCH_KEYWORD = "samsung"
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.nav-line-1-container')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    BUTTON_SEARCH = (By.ID, 'nav-search-submit-button')
    IS_SEARCH_RESULTS_EXITS = (By.CSS_SELECTOR, '.a-spacing-medium')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def go_to_homepage(self):
        self.driver.get(self.WEBSITE)
        home_page_loaded = self.methods.exist_element(By.CSS_SELECTOR, '.a-carousel-center')
        assert home_page_loaded, True

    def go_to_signin_page(self):
        self.methods.wait_element(self.LOGIN_BUTTON).click()

    def search_product(self):

        self.methods.wait_element(
            self.SEARCH_BOX).send_keys(self.SEARCH_KEYWORD)
        self.methods.wait_element(self.BUTTON_SEARCH).click()
        assert self.methods.wait_element(
            self.IS_SEARCH_RESULTS_EXITS).is_displayed(), "Arama sonuçları aktif"

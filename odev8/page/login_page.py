from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class LoginPage:

    EMAIL = ""  # email adresi
    PWD = ""  # şifre
    EMAIL_TEXT = (By.ID, 'ap_email')
    CONTINUE_BTN = (By.ID, 'continue')
    PWD_TEXT = (By.ID, 'ap_password')
    SUBMIT_BTN = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login(self):
        self.methods.wait_element(self.EMAIL_TEXT).send_keys(self.EMAIL)
        self.methods.wait_element(self.CONTINUE_BTN).click()
        self.methods.wait_element(self.PWD_TEXT).send_keys(self.PWD)
        self.methods.wait_element(self.SUBMIT_BTN).click()

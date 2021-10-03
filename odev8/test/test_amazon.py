from selenium import webdriver
from base.page_base import BaseClass
from page.wishlist_page import WishlistPage
from page.category_page import CategoryPage
from page.login_page import LoginPage
from page.main_page import MainPage
from page.product_page import ProductPage
import unittest


class TestCase(unittest.TestCase):
    """Test Case
    1. http://www.amazon.com sitesine gidecek ve anasayfanın açıldığını assertion ile onaylayacak.
    2. Login ekranını açıp, bir kullanıcı ile login olunacak.
    3. Ekranin ustundeki Search alanına 'samsung' yazıp ara butonuna tıklanacak.
    4. Gelen sayfada samsung icin sonuc bulunduğunu onaylayacak.
    5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanin şu an gösterimde oldugunu onaylayacak.
    6. Üstten 3. urunun içindeki 'Add to List' butonuna tıklayacak.
    7. Ekranin en üstündeki 'List' linkine tiklayacak içerisinden Wishlisti seçecek.
    8. Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak.
    9. Favorilere alinan bu urunun yanindaki 'Delete' butonuna basarak, favorilerimden cikaracak.
    10. Sayfada bu urunun artik favorilere alinmadigini onaylayacak.
        """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Users\esra.cakir\Downloads\chromedriver.exe")
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)

    def test_amazon(self):
        self.main_page.go_to_homepage()
        self.main_page.go_to_signin_page()
        self.login_page.login()
        self.main_page.search_product()
        self.category_page.second_page()
        self.category_page.click_product()
        self.product_page.add_product_to_list()
        self.product_page.go_to_wishlist()
        self.wishlist_page.delete_item()
        self.driver.quit()

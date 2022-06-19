from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        product.click()

    def is_product_added_confirm(self):
        product_name_alert = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == product_name_alert, "Incorrect product name"

    def is_price_correct(self):
        price_total = self.browser.find_element(*ProductPageLocators.PRICE_TOTAL).text
        price_of_the_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text
        assert price_of_the_book in price_total, "Incorrect price"
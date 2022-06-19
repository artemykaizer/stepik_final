from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-lg btn-primary btn-add-to-basket')]")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_OF_THE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_FROM_HEADER = (By.CSS_SELECTOR, "span.btn-group a.btn-default")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
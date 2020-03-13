from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div > h1")
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner :nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main> .price_color")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-info  > .alertinner > p > strong")

class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
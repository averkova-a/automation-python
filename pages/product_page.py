from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import  math

class ProductPage(BasePage):
    def add_to_the_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def should_be_right_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART).text
        assert product_name == name_in_cart, "Wrong product name in cart"


    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert product_price == price_in_cart, "Wrong price in cart"

    def should_not_be_succes_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_CART), "Сообщение о добавлении в корзину есть"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_CART)
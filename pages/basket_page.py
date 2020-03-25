from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "There are products in empty basket"

    def should_be_empty_text(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, \
            "No text 'the basket is empty'"
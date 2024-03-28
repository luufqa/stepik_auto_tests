from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        name_before = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BEFORE).text
        price_before = self.browser.find_element(*ProductPageLocators.PRICE_CART_BEFORE).text
        self.find_element_to_be_clickable(ProductPageLocators.ADD_IN_CART).click()
        return name_before, price_before

    def guest_can_add_product_to_basket_info(self):
        #elf.find_element_to_be_clickable(ProductPageLocators.PRODUCT_NAME_AFTER)
        name_after = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER).text
        price_after = self.browser.find_element(*ProductPageLocators.PRICE_CART_AFTER).text
        return name_after, price_after

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

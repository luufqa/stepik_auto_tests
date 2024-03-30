from .locators import ProductPageLocators
from .base_page import BasePage



class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        name_before = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BEFORE).text
        price_before = self.browser.find_element(*ProductPageLocators.PRICE_CART_BEFORE).text
        self.find_element_to_be_clickable(ProductPageLocators.ADD_IN_CART).click()
        return name_before, price_before



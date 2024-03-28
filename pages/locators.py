from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, ".//div[@class='col-sm-6 login_form']")
    REGISTER_FORM = (By.XPATH, ".//div[@class='col-sm-6 register_form']")

class ProductPageLocators:
    ADD_IN_CART = (By.XPATH, ".//button[text()='Добавить в корзину']")
    PRODUCT_NAME_BEFORE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_CART_BEFORE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_AFTER = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRICE_CART_AFTER = (By.CSS_SELECTOR, "div.alertinner > p > strong")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
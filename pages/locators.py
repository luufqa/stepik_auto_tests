from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_EMPTY = (By.ID, "content_inner")
    CART = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, ".//div[@class='col-sm-6 login_form']")
    REGISTER_FORM = (By.XPATH, ".//div[@class='col-sm-6 register_form']")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_ACCEPT = (By.XPATH, ".//*[@value='Register']")
    REGISTER_COMPLETE = (By.XPATH, ".//div[@class='alertinner wicon']")


class ProductPageLocators:
    ADD_IN_CART = (By.XPATH, ".//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME_BEFORE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_CART_BEFORE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_AFTER = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRICE_CART_AFTER = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    # несуществующий локатор (SUCCESS_MESSAGE) необходим для негативного теста в test_product_page.py
    SUCCESS_MESSAGE = (By.ID, "Complete")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_CART = (By.XPATH, './/a[text()="Посмотреть корзину"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

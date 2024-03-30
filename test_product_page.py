from pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time

"""python3 -m pytest -v --tb=line --language=en -m need_review"""
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, '927195093s')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_can_add_product_to_basket(self, browser, setup, link):
        page = ProductPage(browser, link)
        page.open()

        name_before, price_before = page.user_can_add_product_to_basket()
        page.solve_quiz_and_get_code()
        name_after, price_after = page.user_can_add_product_to_basket_info()
        assert name_before == name_after
        assert price_before in price_after


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    name_before, price_before = page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    name_after, price_after = page.user_can_add_product_to_basket_info()
    assert name_before == name_after
    assert price_before in price_after


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_cart()
    assert "Your basket is empty." in page.empty_cart()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


class TestNegative:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        name_before, price_before = page.user_can_add_product_to_basket()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_guest_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        name_before, price_before = page.user_can_add_product_to_basket()
        assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

    """Задание: отрицательные проверки
    Добавьте к себе в проект функции из предыдущего шага и реализуйте несколько простых тестов: 

    test_guest_cant_see_success_message_after_adding_product_to_basket: 
    Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present


    test_guest_cant_see_success_message: 
    Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present


    test_message_disappeared_after_adding_product_to_basket: 
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""

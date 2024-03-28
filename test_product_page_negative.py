from pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    name_before, price_before = page.guest_can_add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER)


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    name_before, price_before = page.guest_can_add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_NAME_AFTER)

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
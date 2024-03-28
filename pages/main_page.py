from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage

class MainPage(BasePage):
    # Инициализация заглушки (т.к. нет методов)
    """super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы
    передали в конструктор MainPage"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

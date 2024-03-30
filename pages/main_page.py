from .base_page import BasePage


class MainPage(BasePage):
    # Инициализация заглушки (т.к. нет методов), методы были перенесены
    """super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы
    передали в конструктор MainPage"""

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

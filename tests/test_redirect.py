import allure

from data import Urls
from pages.main_page import MainPage


class TestRedirect:
    @allure.description("Проверка редиректа со страницы оформления заказа на главную страницу")
    def test_redirect_from_order_page_to_main(self, driver):
        redirect_page = MainPage(driver)
        redirect_page.open_page(Urls.ORDER_PAGE)
        redirect_page.redirect_to_main_page()

        assert driver.current_url == Urls.MAIN_PAGE, "Не удалось перейти на главную страницу Самоката"

    @allure.description("Проверка открытия нового окна и редиректа на Дзен")
    def test_redirect_to_dzen(self, driver):
        redirect_page = MainPage(driver)
        redirect_page.open_page(Urls.MAIN_PAGE)
        redirect_page.redirect_to_dzen()

        assert "dzen.ru" in driver.current_url, "Не удалось перейти на главную страницу Дзена"

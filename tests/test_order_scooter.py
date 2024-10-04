import allure
import pytest
from data import Urls, TestData
from locators.order_page_locators import ScooterOrderPageLocators
from pages.order_page import OrderPage


class TestScooterOrder:

    @pytest.mark.parametrize("order_button, form_data", [
        (ScooterOrderPageLocators.ORDER_BUTTON_TOP, TestData.ORDER_DATA_1),
        (ScooterOrderPageLocators.ORDER_BUTTON_BOTTOM, TestData.ORDER_DATA_2)
    ])
    @allure.description("Проходим весь путь оформления заказа и проверяем, что заказ успешно создан")
    def test_order_top_button(self, driver, order_button, form_data):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.MAIN_PAGE)
        order_page.scroll_and_click(order_button)

        order_page.set_name(form_data)
        order_page.set_surname(form_data)
        order_page.set_address(form_data)
        order_page.set_metro()
        order_page.set_phone(form_data)
        order_page.click_button()
        order_page.set_data()
        order_page.set_submit_order()
        order_page.set_color()
        order_page.set_comment(form_data)

        order_page.submit_order()
        order_page.confirm_order()

        assert order_page.order_successful_displayed(), "Сообщение о подтверждении заказа не отображается."

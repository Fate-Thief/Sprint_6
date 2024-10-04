import allure
import pytest
from data import Urls, TestData
from locators.order_page_locators import ScooterOrderPageLocators
from pages.order_page import OrderPage
from functools import partial

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

        test_pipeline = (
            partial(order_page.set_input, ScooterOrderPageLocators.NAME_INPUT, form_data["name"]),
            partial(order_page.set_input, ScooterOrderPageLocators.SURNAME_INPUT, form_data["surname"]),
            partial(order_page.set_input, ScooterOrderPageLocators.ADDRESS_INPUT, form_data["address"]),
            partial(order_page.click_element, ScooterOrderPageLocators.METRO_INPUT),
            partial(order_page.click_element, ScooterOrderPageLocators.METRO_STATION),
            partial(order_page.set_input, ScooterOrderPageLocators.PHONE_INPUT, form_data["phone"]),
            partial(order_page.click_element, ScooterOrderPageLocators.NEXT_BUTTON),
            partial(order_page.click_element, ScooterOrderPageLocators.DATE_INPUT),
            partial(order_page.click_element, ScooterOrderPageLocators.DATE_SELECT),
            partial(order_page.click_element, ScooterOrderPageLocators.RENTAL_PERIOD_DROPDOWN),
            partial(order_page.click_element, ScooterOrderPageLocators.RENTAL_PERIOD_OPTION),
            partial(order_page.click_element, ScooterOrderPageLocators.GRAY_COLOR_OPTION),
            partial(order_page.set_input, ScooterOrderPageLocators.COMMENT_INPUT, form_data["comment"]),
            partial(order_page.click_element, ScooterOrderPageLocators.SUBMIT_BUTTON_ORDER),
            partial(order_page.click_element, ScooterOrderPageLocators.CONFIRM_BUTTON_ORDER)
        )
        for action in test_pipeline:
            action()

        assert order_page.order_successful_displayed(), "Сообщение о подтверждении заказа не отображается."
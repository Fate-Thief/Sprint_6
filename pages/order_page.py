from pages.base_page import BasePage
from locators.order_page_locators import ScooterOrderPageLocators

class OrderPage(BasePage):

    def set_name(self, form_data):
        name_input = self.wait_and_find_element(ScooterOrderPageLocators.NAME_INPUT)
        name_input.send_keys(form_data["name"])

    def set_surname(self, form_data):
        surname_input = self.wait_and_find_element(ScooterOrderPageLocators.SURNAME_INPUT)
        surname_input.send_keys(form_data["surname"])

    def set_address(self, form_data):
        address_input = self.wait_and_find_element(ScooterOrderPageLocators.ADDRESS_INPUT)
        address_input.send_keys(form_data["address"])

    def set_metro(self):
        metro_input = self.wait_and_find_element(ScooterOrderPageLocators.METRO_INPUT)
        metro_input.click()

        metro_station = self.wait_and_find_element(ScooterOrderPageLocators.METRO_STATION)
        metro_station.click()

    def set_phone(self, form_data):
        phone_input = self.wait_and_find_element(ScooterOrderPageLocators.PHONE_INPUT)
        phone_input.send_keys(form_data["phone"])

    def click_button(self):
        self.click_element(ScooterOrderPageLocators.NEXT_BUTTON)

    def set_data(self):
        data_input = self.wait_and_find_element(ScooterOrderPageLocators.DATE_INPUT)
        data_input.click()

        data_select = self.wait_and_find_element(ScooterOrderPageLocators.DATE_SELECT)
        data_select.click()

    def set_submit_order(self):
        submit_order_input = self.wait_and_find_element(ScooterOrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        submit_order_input.click()

        submit_order = self.wait_and_find_element(ScooterOrderPageLocators.RENTAL_PERIOD_OPTION)
        submit_order.click()

    def set_color(self):
        self.click_element(ScooterOrderPageLocators.GRAY_COLOR_OPTION)

    def set_comment(self, form_data):
        comment_input = self.wait_and_find_element(ScooterOrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(form_data["comment"])

    def submit_order(self):
        self.click_element(ScooterOrderPageLocators.SUBMIT_BUTTON_ORDER)

    def confirm_order(self):
        self.click_element(ScooterOrderPageLocators.CONFIRM_BUTTON_ORDER)

    def order_successful_displayed(self):
        element = self.wait_and_find_element(ScooterOrderPageLocators.ORDER_SUCCESS_MODAL)
        return element.is_displayed()

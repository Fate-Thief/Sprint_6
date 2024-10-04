from selenium.webdriver.common.by import By

class ScooterOrderPageLocators:
    # Локаторы кнопок "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Локаторы формы заказа на 1 странице
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//button[starts-with(@class, 'Order_SelectOption')]/div[text()='Преображенская " 
                               "площадь']")  #  Локатор для определенной станции метро
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы формы заказа на 2 странице
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_SELECT = (By.XPATH, "//div[contains(@class, 'day--006')]")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='пятеро суток']")
    GRAY_COLOR_OPTION = (By.XPATH, "//input[@id='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    SUBMIT_BUTTON_ORDER = (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/button[2]")

    # Локаторы подтверждения заказа
    CONFIRM_BUTTON_ORDER = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[text() ='Заказ оформлен']")

    # Локаторы для хедеров страниц
    HEADER_BUTTON_SCOOTER = (By.XPATH, "//img[@alt = 'Scooter']")
    HEADER_BUTTON_YANDEX = (By.XPATH, "//img[@alt = 'Yandex']")
    DZEN_PAGE = (By.XPATH, "//html[contains(@class, 'zen-page')]")

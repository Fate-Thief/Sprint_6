from selenium.webdriver.common.by import By

class RedirectLocators:

    HEADER_BUTTON_SCOOTER = (By.XPATH, "//img[@alt = 'Scooter']")
    HEADER_BUTTON_YANDEX = (By.XPATH, "//img[@alt = 'Yandex']")
    DZEN_PAGE = (By.XPATH, "//html[contains(@class, 'zen-page')]")

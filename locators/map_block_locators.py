from selenium.webdriver.common.by import By


class MapBlockLocators:

    ADDRESS_A_TEXT = (By.XPATH, "//ymaps[contains(text(), 'Хамовнический Вал, 34')]")
    ADDRESS_B_TEXT = (By.XPATH, "//ymaps[contains(text(), 'Зубовский бульвар, 37')]")
    POINT_A_ID = (By.XPATH, "//ymaps[contains(text(), 'Хамовнический Вал, 34')]/ancestor::ymaps[@id]")
    POINT_B_ID = (By.XPATH, "//ymaps[contains(text(), 'Зубовский бульвар, 37')]/ancestor::ymaps[@id]")
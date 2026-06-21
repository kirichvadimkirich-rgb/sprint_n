import allure
from pages.base_page import BasePage
from locators.map_block_locators import MapBlockLocators


class MapBlock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MapBlockLocators()

    @allure.step("Проверка отображения точки начала маршрута(текст)")
    def is_start_point_displayed(self):
        return self._is_displayed(self.locators.ADDRESS_A_TEXT)

    @allure.step("Проверка отображения точки конца маршрута(текст)")
    def is_end_point_displayed(self):
        return self._is_displayed(self.locators.ADDRESS_B_TEXT)
    
    @allure.step("Получить id цифры для точки А")
    def extract_start_point_id(self):
        return self.extract_point_id(self.locators.POINT_A_ID)
    
    @allure.step("Получить id цифры для точки В")
    def extract_end_point_id(self):
        return self.extract_point_id(self.locators.POINT_B_ID)
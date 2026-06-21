import allure
from pages.base_page import BasePage
from locators.route_select_block_locators import RouteSelectBlockLocators


class RouteSelectBlock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RouteSelectBlockLocators()

    @allure.step("Проверить, что блок выбора маршрута отображается")
    def is_block_select_displayed(self):
        return self._is_displayed(self.locators.ROUTE_OPTIONS_BLOCK)

    # Виды маршрута
    @allure.step("Проверить отображение вида 'Оптимальный'")
    def is_optimal_displayed(self):
        return self._is_displayed(self.locators.MODE_OPTIMAL)

    @allure.step("Проверить отображение вида 'Быстрый'")
    def is_fast_displayed(self):
        return self._is_displayed(self.locators.MODE_FAST)

    @allure.step("Проверить отображение вида 'Свой'")
    def is_custom_displayed(self):
        return self._is_displayed(self.locators.MODE_CUSTOM)

    # Типы передвижения
    @allure.step("Проверить отображение типа 'Машина'")
    def is_car_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_CAR)

    @allure.step("Проверить отображение типа 'Пешком'")
    def is_walk_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_WALK)

    @allure.step("Проверить отображение типа 'Такси'")
    def is_taxi_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_TAXI)

    @allure.step("Проверить отображение типа 'Велосипед'")
    def is_bike_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_BIKE)

    @allure.step("Проверить отображение типа 'Самокат'")
    def is_scooter_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_SCOOTER)

    @allure.step("Проверить отображение типа 'Двайв'")
    def is_drive_displayed(self):
        return self._is_displayed(self.locators.TRANSPORT_DRIVE)

    @allure.step("Проверить отображение стоимости")
    def is_price_displayed(self):
        return self._is_displayed(self.locators.INFO_PRICE)

    @allure.step("Проверить отображение времени в пути")
    def is_time_displayed(self):
        return self._is_displayed(self.locators.INFO_TIME)

    @allure.step("Проверить отображение кнопки 'Вызвать такси'")
    def is_call_taxi_button_displayed(self):
        return self._is_displayed(self.locators.CALL_TAXI_BUTTON)

    @allure.step("Проверить, что текст 'Авто Бесплатно' отображается")
    def is_free_text_displayed(self):
        return self._is_displayed(self.locators.FREE_TEXT)

    @allure.step("Проверить, что текст 'В пути 0 мин.' отображается")
    def is_free_duration_displayed(self):
        return self._is_displayed(self.locators.FREE_DURATION)
    
    @allure.step("Выбрать вид маршрута 'Оптимальный'")
    def go_to_mode_optimal(self):
        self._click(self.locators.MODE_OPTIMAL)

    @allure.step("Получить текст стоимость маршрута")
    def get_price(self):
        return self._get_text(self.locators.INFO_PRICE)

    @allure.step("Получить текст время в пути")
    def get_time(self):
        return self._get_text(self.locators.INFO_TIME)
    
    @allure.step("Получить стоимость маршрута")
    def get_int_price(self):
        return self._extract_number_from_text(self.get_price()) 

    @allure.step("Получить стоимость маршрута")
    def get_int_time(self):
        return self._extract_number_from_text(self.get_time())
     
    @allure.step("Получить первое слово ")
    def get_first_word(self):
        self._get_first_word_from_text(self.get_price())
  

    @allure.step("Проверить, что активен 'Оптимальный'")
    def is_optimal_active(self):
        return self._is_class_active(self.locators.MODE_OPTIMAL)

    @allure.step("Проверить, что активен 'Быстрый'")
    def is_fast_active(self):
        return self._is_class_active(self.locators.MODE_FAST)
    

    @allure.step("Проверить, что кнопка 'Вызвать такси' активна")
    def is_taxi_button_clickable(self):
        return self._is_element_clickable(self.locators.BUTTON_TAXI)
    
    @allure.step("Выбрать вид маршрута 'Оптимальный'")
    def go_to_mode_custom(self):
        self._click(self.locators.MODE_CUSTOM)

    @allure.step("Проверить, что активен 'Свой'")
    def is_custom_active(self):
        return self.is_mode_active(self.locators.MODE_CUSTOM)
    

    allure.step("Проверить, что все типы передвижения активны (не disabled)")
    def are_transport_types_enabled(self):
        elements = self.driver.find_elements(*self.locators.ALL_TRANSPORT_TYPES)
        for elem in elements:
            if "disabled" in elem.get_attribute("class"):
                return False
        return True  
    

    @allure.step("Проверить, что кнопка 'Забронировать' активна")
    def is_book_button_clickable(self):
        return self._is_element_clickable(self.locators.BUTTON_BOOK)
    

    @allure.step("Выбрать тип передвижения 'Драйв'")
    def go_to_type_drive(self):
        self._click(self.locators.TRANSPORT_DRIVE)

    @allure.step("Нажать кнопку 'Вызвать такси'")
    def call_taxi(self):
        self._click(self.locators.BUTTON_TAXI)

    @allure.step("Получить текст стоимость маршрута")
    def get_price_tariff(self):
        return self._get_text(self.locators.PRICE_TARIFF)
    
    @allure.step("Получить стоимость маршрута")
    def get_int_price_tariff(self):
        return self._extract_number_from_text(self.get_price_tariff())
    
    @allure.step("Ожидать, пока 'Свой' станет активным")
    def wait_for_mode_custom_active(self, timeout=10):
        self.wait.until(
            lambda d: "active" in d.find_element(*self.locators.MODE_CUSTOM).get_attribute("class"),
            message=f"Таб 'Свой' не стал активным за {timeout} секунд"
        )

    @allure.step("Проверить, что конкретный вид маршрута активен")
    def is_mode_active(self, mode_locator):
        element = self._wait_for_visibility(mode_locator)
        return "active" in element.get_attribute("class")
       

     
       

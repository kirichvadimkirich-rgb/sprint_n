import allure
from pages.base_page import BasePage
from locators.order_waiting_locators import OrderWaitingLocators
import re


class OrderWaitingBlock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderWaitingLocators()

    @allure.step("Проверить, что открывается окно 'Ожидания машины'")
    def is_displayed_waiting_car_window(self):
        return self._is_displayed(self.locators.WAITING_CAR_TITLE) 

    @allure.step("Получить текст таймера ожидания")
    def get_waiting_timer_text(self):
        return self._get_text(self.locators.WAITING_TIMER)
    
    @allure.step("Проверить, что отображается кнопка 'Отменить'")
    def is_displayed_cancel_button(self):
        return self._is_displayed(self.locators.CANCEL_BUTTON)

    @allure.step("Проверить, что отображается кнопка 'Детали'")
    def is_displayed_details_button(self):
        return self._is_displayed(self.locators.DETAILS_BUTTON)

    @allure.step("Дождаться окончания поиска (исчезновение окна ожидания)")
    def wait_for_search_complete(self, timeout=60):
        self._wait_for_invisibility(self.locators.WAITING_CAR_TITLE, timeout)

    @allure.step("Получить текст заголовка")
    def get_header_title(self):
        return self._get_text(self.locators.HEADER_TITLE)

    @allure.step("Удалить все цифры из загловка")
    def remove_digits_title(self):
      return self._remove_digits(self.get_header_title()) 

    @allure.step("Получить src картинки тарифа")
    def get_tariff_image_src(self):
        element = self._wait_for_presence(self.locators.TARIFF_IMAGE)
        return element.get_attribute("src")
    
    @allure.step("Получить текст номера заказа")
    def get_order_number_text(self):
        return self._get_text(self.locators.ORDER_NUMBER)
    
    @allure.step("Проверить, что номер заказа имеет формат 'буква 3цифры 2буквы'")
    def is_order_number_format_correct(self):
        text = self.get_order_number_text()
        pattern = r'^[A-Za-zА-Яа-я]\s\d{3}\s[A-Za-zА-Яа-я]{2}$'
        return bool(re.match(pattern, text))
    
    @allure.step("Получить имя водителя")
    def get_driver_name(self):
        return self._get_text(self.locators.DRIVER_NAME)
    
    @allure.step("Получить src картинки водителя")
    def get_driver_photo_src(self):
        element = self._wait_for_presence(self.locators.DRIVER_PHOTO)
        return element.get_attribute("src")

    @allure.step("Получить текст рейтинга водителя")
    def get_driver_rating(self):
        return self._get_text(self.locators.DRIVER_RATING)
    
    @allure.step("Нажать кнопку 'Детали'")
    def click_details_button(self):
        self._click(self.locators.DETAILS_BUTTON)

    @allure.step("Получить стоимость из блока деталей")
    def get_details_price(self):
        return self._get_text(self.locators.DETAILS_PRICE)    
    
    @allure.step("Получить стоимость маршрута")
    def get_int_price(self):
        return self._extract_number_from_text(self.get_details_price())
    
    allure.step("Нажать кнопку 'Отмена'")
    def click_cancel_button(self):
        self._click(self.locators.CANCEL_BUTTON)

    @allure.step("Проверить, что окно заказа закрыто (не отображается)")
    def is_order_window_closed(self):
        return not self._is_displayed(self.locators.ORDER_NUMBER )    
   

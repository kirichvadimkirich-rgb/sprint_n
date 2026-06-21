
import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
from data.test_data import TITLE
import re


@allure.feature("Полный флоу заказа такси")
@allure.link(BASE_URL, name='Ссылка на сайт')
class TestOrderFlow:

    @allure.title("Нажатие 'Ввести номер и заказать' открывает окно ожидания")
    @allure.description("Проверить, что 'Заголовок', 'Таймер', кнопки: 'Отменить', 'Детали' отображаются")
    def test_waiting_window_appears(self, route_with_preset_addresses_and_call_taxi):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi
        main_page.order_taxi.open_drop_downn_list_order_requirements()
        main_page.order_taxi.enable_notebook_table()
        main_page.order_taxi.click_submit_order_button()
        timer_text = main_page.order_waiting.get_waiting_timer_text()

        with allure.step("Проверить, что появилось окно ожидания машины"):
            assert main_page.order_waiting.is_displayed_waiting_car_window()

        with allure.step("Проверить, что присутствует таймер"):
            assert re.match(r'\d{2}:\d{2}', timer_text), f"Неверный формат таймера: {timer_text}"

        with allure.step("Проверить, что отображается кнопка 'Отменить'"):
            assert main_page.order_waiting.is_displayed_cancel_button()
        with allure.step("Проверить, что отображается кнопка 'Детали'"):            
            assert main_page.order_waiting.is_displayed_details_button()

        

    @allure.title("После поиска машины отображается окно совершенного заказа")
    @allure.description("Проверить, что 'Заголовок', 'Номер автомобиля и картинка тарифа', Блок с информацией о водителе: Имя, фото, рейтинг, кнопки: 'Отменить', 'Детали' отображаются")
    def test_order_complete_window(self, route_with_preset_addresses_and_call_taxi):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi

        image_tariff = main_page.order_taxi.get_tariff_image_src()

        main_page.order_taxi.open_drop_downn_list_order_requirements()
        main_page.order_taxi.enable_notebook_table()
        main_page.order_taxi.click_submit_order_button() 
        main_page.order_waiting.wait_for_search_complete()

        title = main_page.order_waiting.remove_digits_title()

        image = main_page.order_waiting.get_tariff_image_src()
        
        with allure.step("Сверить текст заголовка"):
            assert title == TITLE , f"Ожидалось '{TITLE}', получено '{title}'"

        with allure.step("Сверить src image тарифа с src image совершенного заказа"):    
            assert image  == image_tariff, f"Ожидалось '{image_tariff}', получено '{image}'"

        with allure.step("Проверить формат номера заказа"):
            assert main_page.order_waiting.is_order_number_format_correct(), f"Номер заказа имеет неверный формат: {main_page.order_waiting.get_order_number_text()}" 

        with allure.step("Проверить, что имя водителя не пустое"):
            driver_name = main_page.order_waiting.get_driver_name()
            assert driver_name.strip(), "Имя водителя не отображается или пустое" 

        with allure.step("Проверить, что картинка водителя не пустая"):
            src = main_page.order_waiting.get_driver_photo_src()
            assert src, "src картинки водителя пустой"

        with allure.step("Проверить, что рейтинг водителя не пустой"):
            rating = main_page.order_waiting.get_driver_rating()
            assert rating.strip(), "Рейтинг водителя пустой"          

        with allure.step("Проверить, что отображается кнопка 'Отменить'"):
            assert main_page.order_waiting.is_displayed_cancel_button()

        with allure.step("Проверить, что отображается кнопка 'Детали'"):            
            assert main_page.order_waiting.is_displayed_details_button



    @allure.title("Стоимость в блоке 'Детали' совпадает с ценой заказа")
    def test_details_price_matches(self, route_with_preset_addresses_and_call_taxi):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi

        price_tariff = main_page.route_select.get_int_price_tariff()

        main_page.order_taxi.open_drop_downn_list_order_requirements()
        main_page.order_taxi.enable_notebook_table()
        main_page.order_taxi.click_submit_order_button()
        main_page.order_waiting.wait_for_search_complete()
        main_page.order_waiting.click_details_button()

        details_price = main_page.order_waiting.get_int_price()
        
        with allure.step("Проверить, что цены совпадают"):
            assert details_price == price_tariff, f"Ожидалось {price_tariff}, получено {details_price}"

    @allure.title("Кнопка 'Отмена' закрывает окно заказа")
    def test_cancel_closes_window(self, route_with_preset_addresses_and_call_taxi_submit_order):
        main_page: MainPage  = route_with_preset_addresses_and_call_taxi_submit_order
        main_page.order_waiting.click_cancel_button()

        with allure.step("Проверить, что окно заказа закрылось"):
            assert main_page.order_waiting.is_order_window_closed()
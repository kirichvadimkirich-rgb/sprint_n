import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
import pytest


@allure.feature("Подготовка к заказу такси")
@allure.link(BASE_URL, name='Ссылка на сайт')
class TestTaxiPrepare:

    @allure.title("Переключение c 'Быстрый' на 'Оптимальный'")
    @allure.description("При переключении меняется активный таб")
    def test_switch_optimal_makes_tab_active(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses
        main_page.route_select.go_to_mode_optimal()
    
        with allure.step("Проверить, что таб 'Оптимальный' стал активным, а таб 'Быстрый'не активен"): 
            assert main_page.route_select.is_optimal_active()
            assert not main_page.route_select.is_fast_active() 


    @allure.title("Переключение c 'Быстрый' на 'Оптимальный'")
    @allure.description("При переключении меняется стоимость и время")
    @pytest.mark.xfail(reason="Время не меняется")
    def test_switch_optimal_changes_price_and_time(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses

        with allure.step("Сохранить стоимость/время, для по умолчанию 'Быстрый'"):
            price_fast = main_page.route_select.get_int_price()
            time_fast = main_page.route_select.get_int_time()
            
        main_page.route_select.go_to_mode_optimal()
           
        with allure.step("Сохранить стоимость/время, для 'Оптимальный'"):
            price_optimal = main_page.route_select.get_int_price()
            time_optimal = main_page.route_select.get_int_time()

        with allure.step("Проверить, что стоимость и время изменились"):    
            assert price_fast != price_optimal
            assert time_fast != time_optimal

    
    @allure.title("При выборе 'Быстрый' (по умолчанию) кнопка 'Вызвать такси' активна")
    @allure.description("В маршруте по умолчанию выбран Быстрый, кнопка вызова такси должна быть доступна")
    def test_taxi_button_active_on_default_fast(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses

        with allure.step("Проверить, что активен вид 'Быстрый'"):
            assert main_page.route_select.is_fast_active()

        with allure.step("Проверить, что кнопка 'Вызвать такси' активна"):
            assert main_page.route_select.is_taxi_button_clickable()

    
    @allure.title("Переключение на 'Свой' активирует все типы передвижения")
    @allure.description("При выборе 'Свой' активный таб становится 'Свой', и все шесть типов передвижения становятся активными")
    def test_switch_custom_enables_transport_types(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses

        with allure.step("Переключиться на вид маршрута 'Свой'"):
            main_page.route_select.go_to_mode_custom()
            main_page.route_select.wait_for_mode_custom_active()

        with allure.step("Проверить, что активен таб 'Свой'"):
            assert main_page.route_select.is_custom_active()

        with allure.step("Проверить, что все типы передвижения активны (не disabled)"):
            assert main_page.route_select.are_transport_types_enabled()

    
    @allure.title("При выборе 'Свой' и типа 'Драйв' кнопка 'Забронировать' активна")
    @allure.description("Для маршрута 'Свой' и типа передвижения 'Драйв' должна появляться активная кнопка 'Забронировать'")
    def test_book_button_active_on_custom_drive(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses

        with allure.step("Выбрать вид маршрута 'Свой'"):
            main_page.route_select.go_to_mode_custom()
            main_page.route_select.wait_for_mode_custom_active()

        with allure.step("Переключиться на тип передвижения 'Драйв'"): 
            main_page.route_select.go_to_type_drive()

        with allure.step("Проверить, что кнопка 'Забронировать' активна"):
            assert main_page.route_select.is_book_button_clickable()


import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
from data.test_data import PRESET_ADDRESS_FROM


@allure.feature("Отрисовка блока с выбором маршрута")
@allure.link(BASE_URL, name='Ссылка на сайт')
class TestRouteSelect:

    @allure.title("Отображение всех элементов блока выбора маршрута")
    @allure.description("При вводе двух разных адресов отображаются виды маршрута, типы передвижения, информация и кнопка")
    def test_route_select_block_displayed_with_different_addresses(selа, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses
        
        with allure.step("Проверить, что блок выбора маршрута отображается"):
            assert main_page.route_select.is_block_select_displayed()

        with allure.step("Проверить виды маршрута"):
            assert main_page.route_select.is_optimal_displayed()
            assert main_page.route_select.is_fast_displayed()
            assert main_page.route_select.is_custom_displayed()

        with allure.step("Проверить типы передвижения"):
            assert main_page.route_select.is_car_displayed()
            assert main_page.route_select.is_walk_displayed()
            assert main_page.route_select.is_taxi_displayed()
            assert main_page.route_select.is_bike_displayed()
            assert main_page.route_select.is_scooter_displayed()
            assert main_page.route_select.is_drive_displayed()

        with allure.step("Проверить информацию о маршруте"):
            assert main_page.route_select.is_price_displayed()
            assert main_page.route_select.is_time_displayed()

        with allure.step("Проверить кнопку 'Вызвать такси'"):
            assert main_page.route_select.is_call_taxi_button_displayed()


    @allure.title("Отображение блока с выбором маршрута при одинаковых адресах")
    @allure.description("При вводе одинакового адреса блок отображается с текстом 'Авто Бесплатно В пути 0 мин.'")
    def test_route_select_block_displayed_with_same_addresses(self, browser):
        main_page = MainPage(browser)
        main_page.input.enter_addresses(PRESET_ADDRESS_FROM, PRESET_ADDRESS_FROM)

        with allure.step("Проверить, что блок выбора маршрута отображается"):
            assert main_page.route_select.is_block_select_displayed()

        with allure.step("Проверить виды маршрута"):
            assert main_page.route_select.is_optimal_displayed()
            assert main_page.route_select.is_fast_displayed()
            assert main_page.route_select.is_custom_displayed()

        with allure.step("Проверить типы передвижения"):
            assert main_page.route_select.is_car_displayed()
            assert main_page.route_select.is_walk_displayed()
            assert main_page.route_select.is_taxi_displayed()
            assert main_page.route_select.is_bike_displayed()
            assert main_page.route_select.is_scooter_displayed()
            assert main_page.route_select.is_drive_displayed()

        with allure.step("Проверить, отображение текста 'Авто Бесплатно В пути 0 мин.'"):
            assert main_page.route_select.is_free_text_displayed()
            assert main_page.route_select.is_free_duration_displayed()
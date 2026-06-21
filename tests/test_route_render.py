import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
from data.test_data import PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO


@allure.feature("Отрисовка маршрута")
@allure.link(BASE_URL, name='Ссылка на сайт')
class TestRouteRender:

    @allure.title("Отображение точек начала и конца маршрута на карте")
    @allure.description("При вводе двух разных адресов на карте отображаются две точки: начала и конца маршрута")
    def test_route_points_are_rendered(self, browser):
        main_page = MainPage(browser)
        main_page.input.enter_addresses(PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO)

        with allure.step("Проверить, что на карте отображается точка начала маршрута"):
            assert main_page.map.is_start_point_displayed(), "Точка начала маршрута не отображается"

        with allure.step("Проверить, что на карте отображается точка конца маршрута"):
            assert main_page.map.is_end_point_displayed(), "Точка конца маршрута не отображается"

    @allure.title("Проверка идентификаторов точек маршрута")
    @allure.description("ID точки конца маршрута должен быть на 1 больше ID точки начала")
    def test_route_point_ids_increment(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses
        start_point_id = main_page.map.extract_start_point_id()
        end_point_id = main_page.map.extract_end_point_id()

        with allure.step("Проверить, что ID точки конца на 1 больше ID точки начала"):
            assert end_point_id == start_point_id + 1, \
                f"Ожидалось {start_point_id + 1}, получено {end_point_id}"
  
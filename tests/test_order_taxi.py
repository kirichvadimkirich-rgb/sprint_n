import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
from data.test_data import TARIFFS_DATA, TARIFF_NAMES 
import pytest


@allure.feature("Заказ тарифа Такси")
@allure.link(BASE_URL, name='Ссылка на сайт')
class TestOrderTaxi:

    @allure.title("Открытие формы заказа такси после нажатия 'Вызвать такси'")
    @allure.description("Проверяем, что форма содержит 6 тарифов, один активный")
    def test_order_taxi_form(self, route_with_preset_addresses):
        main_page: MainPage = route_with_preset_addresses
        main_page.route_select.call_taxi()
        
        with allure.step("Проверить, что тариф 'Рабочий' активный"):
            assert main_page.order_taxi.is_working_tariff_active(), "Активный тариф не 'Рабочий'"
            
        with allure.step("Проверить, что отображаются 6 тарифов"):
            assert  main_page.order_taxi.get_tariffs_count() == 6


    @pytest.mark.parametrize("tariff_name", TARIFF_NAMES, ids=[f"tariff_{name}" for name in TARIFF_NAMES])
    @allure.title("Проверка описания тарифа '{tariff_name}'")
    @allure.description("При наведении на иконку i отображается отображается подсказка")
    def test_tariff_tooltip_displayed(self, route_with_preset_addresses_and_call_taxi, tariff_name):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi
 
        with allure.step(f"Кликнуть на тариф '{tariff_name}'"):
            main_page.order_taxi.click_tariff(tariff_name)

        with allure.step(f"Навести на иконку i тарифа '{tariff_name}'"):
            main_page.order_taxi.hover_over_info_icon(tariff_name)


        with allure.step(f"Проверить, что подсказка открывается"):
            assert main_page.order_taxi.is_tooltip_displayed_by_aria(tariff_name)
       
        
    @pytest.mark.parametrize("tariff_name, expected_desc", TARIFFS_DATA,
                             ids=[f"tariff_{name}" for name, _ in TARIFFS_DATA])
    @allure.title("Проверка описания тарифа '{tariff_name}'")
    @allure.description("При наведении на иконку i отображается корректное описание, соответствующее ТЗ")
    @pytest.mark.xfail(reason="Тариф 'Сонный'- некорреектный текст, Тариф 'Разговорчивый'- некорреектный текст")
    def test_tariff_tooltip(self, route_with_preset_addresses_and_call_taxi, tariff_name, expected_desc):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi
 
        with allure.step(f"Кликнуть на тариф '{tariff_name}'"):
            main_page.order_taxi.click_tariff(tariff_name)

        with allure.step(f"Навести на иконку i тарифа '{tariff_name}'"):
            main_page.order_taxi.hover_over_info_icon(tariff_name)


        with allure.step(f"Получить текст всплывающей подсказки"):
            tooltip_text = main_page.order_taxi.get_tooltip_text()

        with allure.step(f"Проверить, что описание соответствует ТЗ"):
            assert tooltip_text == expected_desc, \
                f"Для тарифа '{tariff_name}' ожидалось '{expected_desc}', получено '{tooltip_text}'"  


    @pytest.mark.parametrize("tariff_name", TARIFF_NAMES, ids=[f"tariff_{name}" for name in TARIFF_NAMES])
    @allure.title("Проверка полей под тарифом '{tariff_name}'")
    @allure.description("Под тарифом присутствую поля: Телефон, Способ оплаты, Комментарий водителю, Требования к заказу, кнопка 'Ввести номер и заказать'")
    def test_tariff_field_form_displayed(self, route_with_preset_addresses_and_call_taxi, tariff_name):
        main_page: MainPage = route_with_preset_addresses_and_call_taxi
 
        with allure.step(f"Кликнуть на тариф '{tariff_name}'"):
            main_page.order_taxi.click_tariff(tariff_name)

        with allure.step(f"Проверить, что поля формы и кнопка отображаются"):
            assert main_page.order_taxi.are_form_fields_displayed()


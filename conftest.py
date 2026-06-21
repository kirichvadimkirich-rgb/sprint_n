import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import BASE_URL
from pages.main_page import MainPage
from data.test_data import PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO


def get_driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def browser(driver):
    driver.get(BASE_URL)
    return driver


@pytest.fixture
def route_with_preset_addresses(browser):
    """Фикстура: Строит маршрут с предустановленными адресами."""
    main_page = MainPage(browser)
    main_page.input.enter_addresses(PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO)
    return main_page

@pytest.fixture
def route_with_preset_addresses_and_call_taxi(browser):
    """Фикстура: Строит маршрут с предустановленными адресами и нажать вызов такси"""
    main_page = MainPage(browser)
    main_page.input.enter_addresses(PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO)
    main_page.route_select.call_taxi()
    return main_page

@pytest.fixture
def route_with_preset_addresses_and_call_taxi_submit_order(browser):
    """Фикстура: Строит маршрут с предустановленными адресами, нажать вызов такси, выбрать столик для ноутбука ,
      нажать заказать, ожидаем поиск машины"""
    main_page = MainPage(browser)
    main_page.input.enter_addresses(PRESET_ADDRESS_FROM, PRESET_ADDRESS_TO)
    main_page.route_select.call_taxi()
    main_page.order_taxi.open_drop_downn_list_order_requirements()
    main_page.order_taxi.enable_notebook_table()
    main_page.order_taxi.click_submit_order_button()
    main_page.order_waiting.wait_for_search_complete()
    return main_page



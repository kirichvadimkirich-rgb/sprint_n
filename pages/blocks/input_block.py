import allure
from pages.base_page import BasePage
from locators.input_block_locators import InputBlockLocators


class InputBlock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = InputBlockLocators()

    @allure.step("Ввести адрес 'Откуда': {address}")
    def set_from(self, address):
        self._send_keys(self.locators.FROM_FIELD, address)

    @allure.step("Ввести адрес 'Куда': {address}")
    def set_to(self, address):
        self._send_keys(self.locators.TO_FIELD, address)


    @allure.step("Ввести адреса 'Откуда' и 'Куда'")
    def enter_addresses(self, from_addr, to_addr):
        self.set_from(from_addr)
        self.set_to(to_addr)
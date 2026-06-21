import allure
from pages.base_page import BasePage
from locators.order_taxi_locators import OrderTaxiLocators
from selenium.webdriver.common.action_chains import ActionChains


class OrderTaxiBlock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderTaxiLocators()

    @allure.step("Навести на иконку информации тарифа {tariff_name}")
    def hover_over_info_icon(self, tariff_name):
        locator = self._format_locator(self.locators.INFO_ICON, tariff_name)
        icon_element = self._wait_for_visibility(locator)   # возвращает WebElement
        ActionChains(self.driver).move_to_element(icon_element).perform()

    @allure.step("Получить текст всплывающего окна")
    def get_tooltip_text(self):
        return self._get_text(self.locators.TOOLTIP_TEXT_TARIFF)

    @allure.step("Проверить, что поля формы и кнопка отображаются")
    def are_form_fields_displayed(self):
        return (self._is_displayed(self.locators.PHONE_FIELD) and
                self._is_displayed(self.locators.PAYMENT_FIELD) and
                self._is_displayed(self.locators.COMMENT_FIELD) and
                self._is_displayed(self.locators.REQUIREMENTS_FIELD) and
                self._is_displayed(self.locators.SUBMIT_ORDER_BUTTON))
    

    @allure.step("Проверить, что активен тариф 'Рабочий'")
    def is_working_tariff_active(self):
        return self._is_class_active(self.locators.ACTIVE_TARIFF)
    
    @allure.step("Получить количество тарифов")
    def get_tariffs_count(self):
        return len(self.driver.find_elements(*self.locators.TARIFF_CARDS))
    
    @allure.step("Выбрать тариф {tariff_name}")
    def click_tariff(self, tariff_name):
        self._click(self._format_locator(self.locators.TARIFF, tariff_name))

    @allure.step("Проверить, что после наведения на иконку тарифа '{tariff_name}' появился атрибут aria-describedby, открывается подсказка")
    def is_tooltip_displayed_by_aria(self, tariff_name):
        locator =  self._format_locator(self.locators.INFO_ICON, tariff_name)
        tooltip = self._wait_for_visibility(locator)
        aria = tooltip.get_attribute("aria-describedby")
        return aria is not None and aria != ""   
    
    @allure.step("Открыть выпадающий список 'Требования к заказу'")
    def open_drop_downn_list_order_requirements(self):
        self._click_by_js(self.locators.REQUIREMENTS_TOGGLE)
   
    @allure.step("Включить чекбокс 'Столик для ноутбука'")
    def enable_notebook_table(self):
        self._click_by_js(self.locators.NOTEBOOK_TABLE_CHECKBOX)

    @allure.step("Нажать кнопку 'Ввести номер и заказать'")
    def click_submit_order_button(self):
        self._click(self.locators.SUBMIT_ORDER_BUTTON)

    @allure.step("Получить src картинки тарифа")
    def get_tariff_image_src(self):
        element = self._wait_for_presence(self.locators.TARIFF_IMAGE)
        return element.get_attribute("src")
            



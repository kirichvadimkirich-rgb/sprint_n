
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import re

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def _is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False


    def _wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))   
    
    def extract_point_id(self, locator):
        id_str = self._get_attribute(locator, "id")
        return int(id_str.split("_")[1])
    
    def _get_attribute(self, locator, attribute_name):
        element = self._wait_for_visibility(locator)
        return element.get_attribute(attribute_name)
    
    def _extract_number_from_text(self, text):
        match = re.search(r'\d+', text)
        if match:
            return int(match.group())
        raise ValueError(f"Число не найдено в тексте: {text}")
    
    def _get_first_word_from_text(self, text):
        if not text:
            return ""
        return text.split()[0]
    
    def _is_element_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
        
    def _is_class_active(self, mode_locator):
        element = self._wait_for_visibility(mode_locator)
        class_attr = element.get_attribute("class")
        return "active" in class_attr    

    @staticmethod
    @allure.step("Форматирование локатора: подстановка '{text}'")
    def _format_locator(locator, text):
        by, value = locator
        return (by, value.format(text)) 
    

    def _click_by_js(self, locator):
        element = self._wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator)) 

    @allure.step("Удалить все цифры из текста")
    def _remove_digits(self, text):
        return re.sub(r'\d+', '', text).strip()      
    
    def _wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    
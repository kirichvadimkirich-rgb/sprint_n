from selenium.webdriver.common.by import By


class OrderTaxiLocators:
    
    TARIFF_CARDS = (By.XPATH, "//div[contains(@class, 'tariff-cards')]//div[contains(@class, 'type')]")
    ACTIVE_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and contains(@class, 'active') and .//div[contains(@class, 'tcard-title') and text()='Рабочий']]")
    TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and  .//div[contains(@class, 'tcard-title') and text()='{}']]")
    INFO_ICON = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(@class, 'tcard-title') and text()='{}']]//button[contains(@customclass, 'tcard-i')]")

    TOOLTIP_TEXT_TARIFF = (By.XPATH, "//div[(@class = 'tcard active')]//div[@class = 'i-dPrefix']")


    PHONE_FIELD =  (By.XPATH, "//div[contains(@class, 'np-text') and text()='Телефон']/parent::div[contains(@class, 'np-button')]")
    PAYMENT_FIELD = (By.XPATH, "//div[contains(@class, 'pp-text') and text()='Способ оплаты']/parent::div[contains(@class, 'pp-button filled')]")
    COMMENT_FIELD = (By.XPATH, "//input[@id='comment']")
    REQUIREMENTS_FIELD = (By.XPATH, "//div[contains(@class, 'reqs-head') and text()='Требования к заказу']/..//..")

    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[.//span[contains(@class, 'smart-button-main') and text()='Ввести номер и заказать']]")
    REQUIREMENTS_TOGGLE = (By.XPATH, "//div[contains(@class, 'reqs-arrow')]")
    NOTEBOOK_TABLE_CHECKBOX = (By.XPATH, "//div[text()='Столик для ноутбука']/following-sibling::div//div[@class = 'switch']")

    TARIFF_IMAGE = (By.XPATH, "//div[contains(@class, 'number')]/following-sibling::img")

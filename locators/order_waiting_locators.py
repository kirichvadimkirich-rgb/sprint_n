from selenium.webdriver.common.by import By

class OrderWaitingLocators:
    WAITING_CAR_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title') and text()='Поиск машины']")

    WAITING_TIMER = (By.XPATH, "//div[contains(@class, 'order-header-time')]")

    CANCEL_BUTTON = (By.XPATH, "//*[text()='Отменить']/preceding-sibling::button")
    DETAILS_BUTTON  = (By.XPATH, "//*[text()='Детали']/preceding-sibling::button")

    HEADER_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title')]")
    TARIFF_IMAGE = (By.XPATH, "//div[contains(@class, 'number')]/following-sibling::img")

    ORDER_NUMBER = (By.XPATH, "//div[@class ='order-body']//div[(@class ='number')]")

    DRIVER_NAME = (By.XPATH, "//div[contains(@class, 'order-buttons')]/div[1]/div[2]")
    DRIVER_PHOTO = (By.XPATH, "//div[@class= 'order-button']//img")
    DRIVER_RATING = (By.XPATH, "//div[contains(@class, 'order-btn-rating')]")

    DETAILS_PRICE = (By.XPATH, "//div[contains(@class, 'order-details-content')]//*[contains(text(), 'Стоимость')]")
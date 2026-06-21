from selenium.webdriver.common.by import By


class RouteSelectBlockLocators:
    # Основной блок (общий контейнер)
    ROUTE_OPTIONS_BLOCK = (By.CLASS_NAME, "workflow-subcontainer")

    # Виды маршрута (Оптимальный, Быстрый, Свой)
    MODE_OPTIMAL = (By.XPATH, "//div[contains(@class, 'mode') and text()='Оптимальный']")
    MODE_FAST = (By.XPATH, "//div[contains(@class, 'mode') and text()='Быстрый']")
    MODE_CUSTOM = (By.XPATH, "//div[contains(@class, 'mode') and text()='Свой']")

    # Типы передвижения (ищем по src картинки, чтобы не зависеть от классов)
    TRANSPORT_CAR = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'car')]")
    TRANSPORT_WALK = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'walk')]")
    TRANSPORT_TAXI = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'taxi')]")
    TRANSPORT_BIKE = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'bike')]")
    TRANSPORT_SCOOTER = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'scooter')]")
    TRANSPORT_DRIVE = (By.XPATH, "//div[contains(@class, 'type')]//img[contains(@src, 'drive')]")

    PRICE_TARIFF = (By.XPATH, "//div[@class ='tcard active']//div[@class='tcard-price']")
    # Информация о маршруте (стоимость, время)
    INFO_PRICE = (By.XPATH, "//div[contains(@class, 'results-text')]//div[contains(text(), 'руб.')]")
    INFO_TIME = (By.XPATH, "//div[contains(@class, 'results-text')]//div[contains(text(), 'мин.')]")

    # Кнопка "Вызвать такси"
    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Вызвать такси']")

    # Текст для одинаковых адресов
    FREE_TEXT = (By.XPATH, "//div[contains(text(), 'Авто Бесплатно')]")
    FREE_DURATION = (By.XPATH, "//div[contains(text(), 'В пути 0 мин.')]")

    BUTTON_TAXI = (By.XPATH, "//button[text()='Вызвать такси']")

    ALL_TRANSPORT_TYPES = (By.XPATH, "//div[contains(@class, 'types-container')]//div[contains(@class, 'type')]")

    BUTTON_BOOK = (By.XPATH, "//button[text()='Забронировать']")
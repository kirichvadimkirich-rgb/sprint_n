
from pages.base_page import BasePage
from pages.blocks.map_block import MapBlock
from pages.blocks.input_block import InputBlock
from pages.blocks.route_select_block import RouteSelectBlock
from pages.blocks.order_taxi_block import OrderTaxiBlock
from pages.blocks.order_waiting_block import OrderWaitingBlock


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.input = InputBlock(driver)
        self.map = MapBlock(driver)
        self.route_select = RouteSelectBlock(driver)
        self.order_taxi = OrderTaxiBlock(driver)
        self.order_waiting = OrderWaitingBlock(driver)

    
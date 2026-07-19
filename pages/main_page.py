from pages.base_page import BasePage
from pages.modal_window import ModalWindow
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def go_to_orders_feed(self):
        self.click(MainPageLocators.ORDERS_FEED_BUTTON)

    def click_ingredient(self, ingredient_name: str):
        locator = MainPageLocators.ingredient_locator(ingredient_name)
        self.find_element(locator).click()
        return ModalWindow(self.driver)

    def get_ingredient_counter(self, ingredient_name: str) -> str:
        locator = MainPageLocators.ingredient_counter_locator(ingredient_name)
        return self.get_text(locator)

    def add_ingredient_to_order(self, ingredient_name: str):
        locator = MainPageLocators.ingredient_locator(ingredient_name)
        self.find_element(locator).click()

    def place_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        return self.get_order_number_after_creation()

    def get_order_number_after_creation(self) -> str:
        return self.get_text(MainPageLocators.ORDER_NUMBER)

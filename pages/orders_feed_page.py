from pages.base_page import BasePage
from locators.orders_feed_page_locators import OrdersFeedPageLocators

class OrdersFeedPage(BasePage):
    def get_total_orders_count(self) -> int:
        return int(self.get_text(OrdersFeedPageLocators.TOTAL_COUNTER))

    def get_today_orders_count(self) -> int:
        return int(self.get_text(OrdersFeedPageLocators.TODAY_COUNTER))

    def get_orders_in_work(self) -> list:
        elements = self.find_elements(OrdersFeedPageLocators.ORDER_IN_WORK)
        return [el.text for el in elements]

    def wait_for_order_appear(self, timeout=10):
        self.wait.until(lambda d: len(d.find_elements(*OrdersFeedPageLocators.ORDER_IN_WORK)) > 0)

from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(text(), 'Конструктор')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed') and contains(text(), 'Лента заказов')]")
    BUN_COUNTER = (By.XPATH, "//div[contains(@data-testid, 'bun')]//p[contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'OrderDetails')]//h2")

    @staticmethod
    def ingredient_locator(ingredient_name: str):
        return (By.XPATH, f"//div[contains(@class, 'ingredient')]//p[text()='{ingredient_name}']/..")

    @staticmethod
    def ingredient_counter_locator(ingredient_name: str):
        return (By.XPATH, f"//div[contains(@data-testid, 'ingredient')]//p[text()='{ingredient_name}']/../..//p[contains(@class, 'counter')]")

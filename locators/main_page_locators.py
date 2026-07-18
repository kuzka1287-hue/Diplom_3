from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(text(), 'Конструктор')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed') and contains(text(), 'Лента заказов')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredient') and contains(@data-testid, 'ingredient')]")
    BUN_COUNTER = (By.XPATH, "//div[contains(@data-testid, 'bun')]//p[contains(@class, 'counter')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@data-testid, 'ingredient')]//p[contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'OrderDetails')]//h2")

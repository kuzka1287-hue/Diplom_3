from selenium.webdriver.common.by import By

class OrdersFeedPageLocators:
    TOTAL_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'orderList')]//li[contains(@class, 'order')]")

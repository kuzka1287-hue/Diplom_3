from selenium.webdriver.common.by import By

class ModalWindowLocators:
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'modal')]//h2")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'modal')]//div[contains(@class, 'content')]")

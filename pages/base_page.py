from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    # Новые методы
    def get_current_url(self) -> str:
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    def get_cookie_value(self, name: str) -> str:
        cookie = self.driver.get_cookie(name)
        return cookie["value"] if cookie else None

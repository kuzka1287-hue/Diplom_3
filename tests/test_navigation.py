import allure
from pages.main_page import MainPage

@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход на страницу 'Конструктор' по клику")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed()
        main_page.go_to_constructor()
        current_url = main_page.get_current_url()
        assert "constructor" in current_url or "stellarburgers" in current_url

    @allure.title("Переход на страницу 'Лента заказов' по клику")
    def test_click_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_feed()
        current_url = main_page.get_current_url()
        assert "/feed" in current_url

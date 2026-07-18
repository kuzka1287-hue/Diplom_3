import allure
import requests
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from data import BASE_URL, ORDERS_ENDPOINT, INGREDIENT_IDS

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_orders_counter_increases(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.go_to_orders_feed()
        feed_page = OrdersFeedPage(logged_in_driver)
        initial_total = feed_page.get_total_orders_count()
        main_page.go_to_constructor()
        token = main_page.get_cookie_value("accessToken")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.post(BASE_URL + ORDERS_ENDPOINT,
                                 json={"ingredients": INGREDIENT_IDS},
                                 headers=headers)
        assert response.status_code == 200, "Не удалось создать заказ через API"
        main_page.refresh_page()
        main_page.go_to_orders_feed()
        new_total = feed_page.get_total_orders_count()
        assert new_total > initial_total, "Счётчик 'за всё время' не увеличился"

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_orders_counter_increases(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.go_to_orders_feed()
        feed_page = OrdersFeedPage(logged_in_driver)
        initial_today = feed_page.get_today_orders_count()
        main_page.go_to_constructor()
        token = main_page.get_cookie_value("accessToken")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.post(BASE_URL + ORDERS_ENDPOINT,
                                 json={"ingredients": INGREDIENT_IDS},
                                 headers=headers)
        assert response.status_code == 200, "Не удалось создать заказ через API"
        main_page.refresh_page()
        main_page.go_to_orders_feed()
        new_today = feed_page.get_today_orders_count()
        assert new_today > initial_today, "Счётчик 'за сегодня' не увеличился"

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_work_section(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.go_to_orders_feed()
        feed_page = OrdersFeedPage(logged_in_driver)
        main_page.go_to_constructor()
        main_page.add_ingredient_to_order("Говяжий метеорит")
        main_page.add_ingredient_to_order("Соус традиционный")
        main_page.place_order()
        order_number = main_page.get_order_number_after_creation()
        main_page.go_to_orders_feed()
        orders_in_work = feed_page.get_orders_in_work()
        assert str(order_number) in orders_in_work, \
            f"Номер заказа {order_number} не появился в 'В работе'"

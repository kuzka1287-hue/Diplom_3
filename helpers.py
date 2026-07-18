# helpers.py

import requests
import random
import string
from data import BASE_URL, REGISTER_ENDPOINT, ORDERS_ENDPOINT


def generate_user_data():
    """Генерирует уникальные данные для пользователя."""
    letters = string.ascii_lowercase + string.digits
    random_part = ''.join(random.choice(letters) for _ in range(6))
    return {
        "email": f"test_{random_part}@yandex.ru",
        "password": "password123",
        "name": f"User_{random_part}"
    }


def register_user(user_data):
    """Отправляет запрос на регистрацию и возвращает ответ."""
    url = BASE_URL + REGISTER_ENDPOINT
    return requests.post(url, json=user_data)


def delete_user(access_token):
    """
    Удаляет пользователя (заглушка, так как API не поддерживает удаление).
    В реальном проекте здесь должен быть вызов DELETE /api/auth/user.
    """
    # Если бы эндпоинт существовал:
    # url = BASE_URL + "/api/auth/user"
    # headers = {"Authorization": access_token}
    # requests.delete(url, headers=headers)
    pass


def create_order(token: str, ingredients: list):
    """
    Отправляет запрос на создание заказа.
    Не проверяет статус ответа — это остаётся на усмотрение теста.
    """
    url = BASE_URL + ORDERS_ENDPOINT
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json={"ingredients": ingredients}, headers=headers)

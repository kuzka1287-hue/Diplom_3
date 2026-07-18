import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from data import BASE_URL
from helpers import register_user, delete_user, generate_user_data


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    """Создаёт пользователя, возвращает данные и токен. Постусловие – удаление."""
    user_data = generate_user_data()
    response = register_user(user_data)
    json_data = response.json()
    access_token = json_data.get("accessToken")
    yield {
        "user": user_data,
        "access_token": access_token,
        "refresh_token": json_data.get("refreshToken")
    }
    if access_token:
        delete_user(access_token)   # заглушка


@pytest.fixture
def logged_in_driver(driver, registered_user):
    """Устанавливает токен в куки для авторизации."""
    token = registered_user["access_token"]
    if token and token.startswith("Bearer "):
        token = token.replace("Bearer ", "")
    driver.add_cookie({"name": "accessToken", "value": token})
    driver.refresh()
    return driver

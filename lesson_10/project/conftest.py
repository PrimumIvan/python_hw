"""Общие фикстуры pytest для тестов SauceDemo."""

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> WebDriver:
    """Создаёт экземпляр Firefox и закрывает его после теста.

    Yields:
        WebDriver: Экземпляр браузера Firefox с неявным ожиданием
        5 секунд.
    """
    with allure.step("Запустить браузер Firefox"):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()

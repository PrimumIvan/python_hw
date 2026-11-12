"""Тест подмены сессии: два пользователя, разные куки, разные профили."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://gitflic.ru/'
TIMEOUT = 10

USER1_COOKIES = [{'name': 'SESSION', 'value': 'ВАШЕ_ЗНАЧЕНИЕ_1',
                  'domain': '.gitflic.ru', 'path': '/'}]
USER2_COOKIES = [{'name': 'SESSION', 'value': 'ВАШЕ_ЗНАЧЕНИЕ_2',
                  'domain': '.gitflic.ru', 'path': '/'}]

# Реальные URL профилей — замените на свои (откройте профиль в браузере и скопируйте)
USER1_PROFILE_URL = 'https://gitflic.ru/user/username1'
USER2_PROFILE_URL = 'https://gitflic.ru/user/username2'


def test_session_storage_auth():
    """Устанавливает куки двух пользователей и проверяет, что URL профилей различаются."""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        # Открыта страница
        driver.get(BASE_URL)

        # Куки пользователя 1
        for cookie in USER1_COOKIES:
            driver.add_cookie(cookie)

        # Обновление страницы
        driver.refresh()

        # Переход на профиль пользователя 1 и сохранение URL
        driver.get(USER1_PROFILE_URL)
        wait.until(EC.url_contains(USER1_PROFILE_URL))
        url_user1 = driver.current_url

        # Очистка куки
        driver.delete_all_cookies()

        # Куки пользователя 2
        driver.get(BASE_URL)
        for cookie in USER2_COOKIES:
            driver.add_cookie(cookie)
        driver.refresh()

        # Переход на профиль пользователя 2 и сохранение URL
        driver.get(USER2_PROFILE_URL)
        wait.until(EC.url_contains(USER2_PROFILE_URL))
        url_user2 = driver.current_url

        # Скриншот итогового состояния
        driver.save_screenshot('profiles.png')

        # Проверка различия URL
        assert url_user1 != url_user2, (
            f'URL пользователей совпадают: {url_user1}'
        )
    finally:
        driver.quit()
        
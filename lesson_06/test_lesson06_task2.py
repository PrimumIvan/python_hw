from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    base_url = 'https://gitflic.ru/'

    user1_cookies = [
        {
            'name': 'SESSION',
            'value': 'значение_сессии_первого_пользователя',
            'domain': 'gitflic.ru',
            'path': '/',
        }
    ]
    user2_cookies = [
        {
            'name': 'SESSION',
            'value': 'значение_сессии_второго_пользователя',
            'domain': 'gitflic.ru',
            'path': '/',
        }
    ]

    user1_profile_url = 'https://gitflic.ru'
    user2_profile_url = 'https://gitflic.ru'

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        for cookie in user1_cookies:
            driver.add_cookie(cookie)
        driver.refresh()

        wait.until(
            EC.invisibility_of_element_located((By.LINK_TEXT, 'Войти'))
        )

        driver.get(user1_profile_url)
        wait.until(EC.url_contains('username1'))
        url_user1 = driver.current_url

        driver.delete_all_cookies()
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Войти')))

        for cookie in user2_cookies:
            driver.add_cookie(cookie)
        driver.refresh()

        wait.until(
            EC.invisibility_of_element_located((By.LINK_TEXT, 'Войти'))
        )

        driver.get(user2_profile_url)
        wait.until(EC.url_contains('username2'))
        url_user2 = driver.current_url

        assert url_user1 != url_user2, (
            f'URL пользователей совпадают: {url_user1}'
        )

    finally:
        driver.quit()
        
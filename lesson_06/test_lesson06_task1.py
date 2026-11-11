from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://the-internet.herokuapp.com/dynamic_loading/2'
TIMEOUT = 10


def test_dynamic_loading():
    """Клик по Start, ожидание 'Hello World!', скриншот и проверка текста."""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        driver.get(URL)

        # Оптимальный локатор: id контейнера start + кнопка внутри
        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#start button'))
        )
        start_button.click()

        # Ждём появления текста после загрузки (div скрыт до завершения)
        finish_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4'))
        )

        driver.save_screenshot('hello_world.png')

        expected_text = 'Hello World!'
        actual_text = finish_element.text
        assert actual_text == expected_text, (
            f"Ожидался текст '{expected_text}', но получен '{actual_text}'"
        )
    finally:
        driver.quit()
      
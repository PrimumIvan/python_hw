from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        url = 'https://the-internet.herokuapp.com/dynamic_loading/2'
        driver.get(url)

        start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
        start_button.click()

        wait = WebDriverWait(driver, 10)
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
        
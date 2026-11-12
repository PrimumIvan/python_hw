from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    """Проверка калькулятора с задержкой: 7 + 8 = 15 отобразится через 45 сек."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        wait = WebDriverWait(driver, 50)

        # Вводим задержку 45 секунд
        delay_field = driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys("45")

        # Нажимаем кнопки 7, +, 8, =
        for button_text in ["7", "+", "8", "="]:
            driver.find_element(
                By.XPATH, f"//span[text()='{button_text}']"
            ).click()

        # Ждём результат: он появится только через 45 секунд после "="
        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        wait.until(lambda d: screen.text.strip() == "15")

        # Финальная проверка
        assert screen.text.strip() == "15", (
            f"Ожидался результат 15, получен: {screen.text}"
        )

    finally:
        driver.quit()

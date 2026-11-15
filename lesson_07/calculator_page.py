from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    # Локаторы элементов
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, seconds: int):
        """Очищает поле задержки и вводит новое значение."""
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text: str):
        """Нажимает на кнопку калькулятора по её тексту."""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, expected_result: str, timeout: int = 46) -> str:
        """Ожидает появления результата на экране и возвращает его."""
        WebDriverWait(self.driver, timeout).until(
            ec.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        return self.driver.find_element(*self.SCREEN).text

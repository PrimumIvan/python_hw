"""Page Object страницы оформления заказа магазина SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Страницы оформления заказа (checkout-step-one/step-two).

    Содержит методы для заполнения данных покупателя и чтения
    итоговой стоимости заказа.
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: Экземпляр WebDriver, управляющий браузером.
        """
        self.driver = driver

    def fill_customer_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет данные покупателя и нажимает Continue.

        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            postal_code: Почтовый индекс покупателя.

        Returns:
            None.
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(
            first_name
        )
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(
            last_name
        )
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self) -> float:
        """Извлекает итоговую сумму заказа со страницы Overview.

        Returns:
            float: Итоговая сумма заказа с учётом налога,
            например 58.29.
        """
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        return float(total_text.replace("Total: $", ""))

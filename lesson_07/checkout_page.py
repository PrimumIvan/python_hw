from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_customer_info(
        self, first_name: str, last_name: str, postal_code: str
    ):
        """Заполняет данные покупателя и нажимает Continue."""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self) -> str:
        """Извлекает итоговую сумму (например, '$58.29') со страницы."""
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        return total_text.replace("Total: ", "")

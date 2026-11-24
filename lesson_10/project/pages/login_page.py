"""Page Object страницы авторизации магазина SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Страница авторизации (saucedemo.com).

    Содержит методы для открытия сайта и входа под учётной записью.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу авторизации.

        Args:
            driver: Экземпляр WebDriver, управляющий браузером.
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации.

        Returns:
            None.
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """Вводит логин, пароль и нажимает кнопку входа.

        Args:
            username: Логин пользователя.
            password: Пароль пользователя.

        Returns:
            None.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

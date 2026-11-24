"""Page Object страницы каталога товаров магазина SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Страница каталога товаров (inventory.html).

    Содержит методы для добавления товаров в корзину и перехода
    на страницу корзины.
    """

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу каталога.

        Args:
            driver: Экземпляр WebDriver, управляющий браузером.
        """
        self.driver = driver

    def add_item_to_cart(self, item_name: str) -> None:
        """Добавляет товар в корзину по его названию.

        Args:
            item_name: Название товара, как оно отображается
                в каталоге, например "Sauce Labs Backpack".

        Returns:
            None.
        """
        xpath = (
            f"//div[@class='inventory_item_name' "
            f"and text()='{item_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self) -> None:
        """Переходит на страницу корзины по ссылке с иконкой корзины.

        Returns:
            None.
        """
        self.driver.find_element(*self.CART_LINK).click()

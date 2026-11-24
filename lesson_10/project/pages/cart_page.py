"""Page Object страницы корзины магазина SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Страница корзины (cart.html).

    Содержит локаторы и методы для работы с товарами корзины
    и переходом к оформлению заказа.
    """

    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: Экземпляр WebDriver, управляющий браузером.
        """
        self.driver = driver

    def get_cart_items(self) -> list[str]:
        """Возвращает список названий всех товаров в корзине.

        Returns:
            list[str]: Список названий товаров в порядке добавления.
        """
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout и переходит к оформлению заказа.

        Returns:
            None.
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

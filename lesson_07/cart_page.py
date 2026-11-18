from selenium.webdriver.common.by import By


class CartPage:
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self) -> list[str]:
        """Возвращает список названий всех товаров в корзине."""
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def click_checkout(self):
        """Нажимает кнопку Checkout."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name: str):
        """Добавляет товар в корзину по его названию."""
        xpath = (
            f"//div[text()='{item_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        """Переходит на страницу корзины."""
        self.driver.find_element(*self.CART_LINK).click()

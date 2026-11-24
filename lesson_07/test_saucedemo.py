from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_saucedemo_checkout():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Открыть сайт и авторизоваться
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Добавить три товара в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

        # 3. Перейти в корзину и проверить содержимое
        inventory_page.go_to_cart()
        assert cart_page.get_cart_items() == items_to_add

        # 4. Нажать Checkout и заполнить форму
        cart_page.click_checkout()
        checkout_page.fill_customer_info("Василий", "Пупкин", "143981")

        # 5. Прочитать итоговую стоимость
        total_price = checkout_page.get_total_price()
    finally:
        # 6. Закрыть браузер
        driver.quit()

    # 7. Проверить, что итоговая сумма равна $58.29
    assert total_price == "$58.29", (
        f"Ожидалась сумма '$58.29', но получено '{total_price}'"
    )

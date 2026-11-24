"""E2E-тест полного пути покупки в магазине SauceDemo."""

import allure
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

TAX_RATE = 0.08


@allure.title("Успешное оформление заказа в SauceDemo")
@allure.description(
    "Полный путь пользователя: авторизация, добавление трёх товаров "
    "в корзину, проверка содержимого корзины, заполнение данных "
    "покупателя и проверка итоговой суммы с учётом налога 8%."
)
@allure.feature("Оформление заказа (Checkout)")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    items_sum = 29.99 + 15.99 + 7.99
    expected_total = round(items_sum * (1 + TAX_RATE), 2)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step(f"Добавить в корзину товары: {items_to_add}"):
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Проверить, что корзина содержит добавленные товары"):
        cart_items = cart_page.get_cart_items()
        assert cart_items == items_to_add, (
            f"Ожидались товары {items_to_add}, "
            f"но в корзине {cart_items}"
        )

    with allure.step("Нажать Checkout и заполнить данные покупателя"):
        cart_page.click_checkout()
        checkout_page.fill_customer_info("Василий", "Пупкин", "143981")

    with allure.step("Прочитать итоговую стоимость заказа"):
        total_price = checkout_page.get_total_price()

    with allure.step(
        f"Проверить, что итоговая сумма равна {expected_total}"
    ):
        assert total_price == pytest.approx(expected_total), (
            f"Ожидалась сумма {expected_total:.2f}, "
            f"но получено {total_price}"
        )

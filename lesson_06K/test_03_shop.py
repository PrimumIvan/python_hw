from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_saucedemo_checkout():
    """Проверка итоговой суммы заказа: три товара, checkout, total $58.29."""
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        # 1 - Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 2 - Добавляем три товара в корзину
        items = ["backpack", "bolt-t-shirt", "onesie"]
        for item in items:
            driver.find_element(
                By.ID, f"add-to-cart-sauce-labs-{item}"
            ).click()

        # 3 - Переходим в корзину
        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        # 4 - Нажимаем Checkout
        driver.find_element(By.ID, "checkout").click()

        # Итог - Заполняем форму данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Читаем итоговую стоимость со страницы
        total_label = wait.until(
            lambda d: d.find_element(
                By.CSS_SELECTOR, "div.summary_total_label"
            )
        )
        total_text = total_label.text  # например: "Total: $58.29"
        total_value = total_text.split("$")[-1]

        # Закрываем браузер до проверок
        driver.quit()

        assert total_value == "58.29", (
            f"Ожидалась сумма $58.29, получено: {total_text}"
        )

    finally:
        driver.quit()
        
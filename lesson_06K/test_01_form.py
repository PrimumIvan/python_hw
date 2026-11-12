from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_data_types_form():
    """Для Windows используеем Edge: пустой zip-code подсвечен красным, остальные — зелёным."""
    driver = webdriver.Edge()
    driver.maximize_window()

    url = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        for field_name, value in form_data.items():
            if value:
                element = driver.find_element(By.ID, field_name)
                element.send_keys(value)

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_button.click()

        zip_code_div = wait.until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )

        assert "alert-danger" in zip_code_div.get_attribute("class"), (
            "Поле Zip code не подсвечено красным"
        )

        for field_id in form_data:
            if field_id == "zip-code":
                continue

            element = driver.find_element(By.ID, field_id)
            assert "alert-success" in element.get_attribute("class"), (
                f"Поле {field_id} не подсвечено зелёным"
            )

    finally:
        driver.quit()
        
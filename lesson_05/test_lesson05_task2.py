from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    initial_url = driver.current_url

    name_input = driver.find_element(By.NAME, "custname")

    name_input.send_keys("Гена")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit']"
    )
    submit_button.click()

    assert driver.current_url != initial_url, (
        f"Действие не привело к смене URL. "
        f"Текущий URL: {driver.current_url}"
    )

    driver.quit()
    
from selenium.webdriver.common.by import By


def perform_login(driver):

    username = driver.find_element(
        By.XPATH, '//input[starts-with(@id, "txt-username")]'
    )
    username.clear()
    username.send_keys("John Doe")
    username.click()

    password = driver.find_element(
        By.XPATH, "/html/body/section/div/div/div[2]/form/div[3]/div/input"
    )
    password.clear()
    password.send_keys("ThisIsNotAPassword")
    password.click()

    driver.find_element(By.XPATH, '//button[text()="Login"]').click()

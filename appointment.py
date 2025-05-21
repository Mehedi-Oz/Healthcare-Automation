import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def make_appointment(driver):

    facility = driver.find_element(
        By.XPATH, "//select[@id='combo_facility' and @name='facility']"
    )

    facilities = Select(facility)
    facilities.select_by_value("Seoul CURA Healthcare Center")

    driver.find_element(
        By.XPATH, "//label[@for='chk_hospotal_readmission']//child::input"
    ).click()

    driver.find_element(By.XPATH, "//input[@value='Medicaid']").click()

    driver.find_element(By.XPATH, '//*[@id="txt_visit_date"]').click()

    visit_month = "May 2026"

    click_next_to_calender = driver.find_element(
        By.XPATH, "/html/body/div/div[1]/table/thead/tr[2]/th[3]"
    )

    while True:
        month_year = driver.find_element(
            By.XPATH, "/html/body/div/div[1]/table/thead/tr[2]/th[2]"
        )
        if month_year.text == visit_month:
            break
        click_next_to_calender.click()

    visit_day = driver.find_element(
        By.XPATH, "/html/body/div/div[1]/table/tbody/tr[4]/td[3]"
    )
    visit_day.click()

    comment = driver.find_element(By.XPATH, '//*[@id="txt_comment"]')
    comment.clear()
    comment.send_keys("This is a comment!")

    book_appoinment = driver.find_element(By.XPATH, '//*[@id="btn-book-appointment"]')
    book_appoinment.click()
    time.sleep(1)


def handle_appointment_confirmation(driver):

    back_to_homepage = driver.find_element(
        By.XPATH, '//*[@id="summary"]/div/div/div[7]/p/a'
    )
    back_to_homepage.click()
    time.sleep(1)

    nav_bar = driver.find_element(By.XPATH, '//*[@id="menu-toggle"]')
    nav_bar.click()

    history = driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[3]/a')
    history.click()
    time.sleep(1)

    nav_bar = driver.find_element(By.XPATH, '//*[@id="menu-toggle"]')
    nav_bar.click()

    logout = driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[5]/a')
    logout.click()

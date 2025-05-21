import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login import perform_login
from appointment import make_appointment, handle_appointment_confirmation

# Initialize driver
driver = webdriver.Edge()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# Login
driver.find_element(By.XPATH, "//a[contains(@id, 'btn-make-appointment')]").click()
perform_login(driver)

# Appointment
make_appointment(driver)

# Checking History and Logging Out
handle_appointment_confirmation(driver)

# Close browser
time.sleep(1)
driver.close()

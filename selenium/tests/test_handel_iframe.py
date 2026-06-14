import time
from selenium.webdriver.common.by import By

def test_handel_iframe(driver):
    driver.get("https://testing.qaautomationlabs.com/iframe.php")
    time.sleep(2)
    driver.switch_to.frame("iframe1")
    driver.find_element(By.XPATH, "//button[normalize-space()='CLick Me']").click()
    time.sleep(2)
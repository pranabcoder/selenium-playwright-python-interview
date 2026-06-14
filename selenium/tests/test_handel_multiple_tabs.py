import time

from selenium.webdriver.common.by import By

def test_handel_multiple_tabs(driver):
    driver.get("https://demo.automationtesting.in/Windows.html")
    driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
    time.sleep(2)
    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()
        time.sleep(2)
        driver.quit()
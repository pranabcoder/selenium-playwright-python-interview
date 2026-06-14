import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_right_click(driver):
    driver.get("https://vinothqaacademy.com/mouse-event/")
    right_clicked_button_path = driver.find_element(By.XPATH, "//button[@id='rightBtn']")
    ActionChains(driver).context_click(right_clicked_button_path).perform()
    time.sleep(2)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_mouse_over(driver):
    driver.get("https://practice-automation.com/hover/")
    time.sleep(2)
    hover_item_path = driver.find_element(By.XPATH, "//h3[@id='mouse_over']")
    action = ActionChains(driver)
    action.move_to_element(hover_item_path).perform()
    time.sleep(2)
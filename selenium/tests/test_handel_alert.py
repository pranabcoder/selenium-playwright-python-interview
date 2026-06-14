import time
from selenium.webdriver.common.by import By

def test_handel_alert(driver):
    driver.get('https://demoqa.com/alerts')
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(5)
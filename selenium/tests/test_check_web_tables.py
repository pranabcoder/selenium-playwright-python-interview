import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_web_tables(driver):
    driver.get('https://vinothqaacademy.com/webtable/')
    driver.maximize_window()
    time.sleep(5)

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employeeTable"))
    )

    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        print([col.text for col in cols])

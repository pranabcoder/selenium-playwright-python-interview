import time

def test_check_screenshot(driver):
    driver.get("https://demo.automationtesting.in/Windows.html")
    time.sleep(2)
    driver.save_screenshot("screenshot.png")
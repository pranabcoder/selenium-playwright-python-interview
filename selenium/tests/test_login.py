import time
from pages.LoginPage import LoginPage

def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    time.sleep(5)
    login_page.enter_username("Admin")
    time.sleep(2)
    login_page.enter_password("admin123")
    login_page.click_login()
    time.sleep(10)
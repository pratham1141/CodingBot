from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username("test_user")
    login.enter_password("secure_pass")
    login.click_login()
    assert login.is_login_successful()

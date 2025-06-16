class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("http://example.com/login")

    def enter_username(self, username):
        self.driver.find_element_by_id("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id("login").click()

    def is_login_successful(self):
        return "dashboard" in self.driver.current_url

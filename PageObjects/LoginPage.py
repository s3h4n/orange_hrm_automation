from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    """Page Object for the Login Page"""

    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    LOGIN_PAGE_HEADER = (By.XPATH, "//h5[text()='Login']")

    # Page title
    LOGIN_PAGE_TITLE = "OrangeHRM"

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self):
        """Get the title of the login page"""
        return self.get_title()

    def is_login_page_loaded(self):
        """Check if login page is loaded by verifying the header"""
        return self.is_visible(*self.LOGIN_PAGE_HEADER)

    def set_username(self, username):
        """Enter username in the username field"""
        self.send_text(*self.USERNAME_INPUT, username)

    def set_password(self, password):
        """Enter password in the password field"""
        self.send_text(*self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click on the login button"""
        self.click_element(*self.LOGIN_BUTTON)

    def login(self, username, password):
        """Login with the given credentials"""
        self.set_username(username)
        self.set_password(password)
        self.click_login()
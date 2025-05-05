import pytest
import time
import allure
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
from Utilities.ReadConfig import ReadConfig


@pytest.mark.usefixtures("setup")
class TestOrangeHRM:
    """Test class for OrangeHRM application"""

    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Verify login page title")
    def test_login_page_title(self):
        """Test to verify login page title"""
        self.driver.get(self.base_url)
        time.sleep(2)  # Wait for page to load

        login_page = LoginPage(self.driver)
        page_title = login_page.get_login_page_title()

        assert "OrangeHRM" in page_title, f"Expected 'OrangeHRM' in title, but got '{page_title}'"
        assert login_page.is_login_page_loaded(), "Login page is not loaded correctly"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Verify login functionality")
    def test_login_functionality(self):
        """Test to verify login functionality"""
        self.driver.get(self.base_url)
        time.sleep(2)  # Wait for page to load

        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        time.sleep(3)  # Wait for login

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.is_dashboard_loaded(), "Dashboard page is not loaded after login"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Verify leave functionality")
    def test_leave_functionality(self):
        """Test to verify leave functionality by clicking My Leave icon"""
        self.driver.get(self.base_url)
        time.sleep(2)  # Wait for page to load

        # Login first
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        time.sleep(3)  # Wait for login

        # Navigate to Leave page
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_my_leave()
        time.sleep(3)  # Wait for leave page to load

        # Verify Leave page is loaded
        leave_page = LeavePage(self.driver)
        assert leave_page.is_leave_page_loaded(), "Leave page is not loaded correctly"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Verify logout functionality")
    def test_logout_functionality(self):
        """Test to verify logout functionality"""
        self.driver.get(self.base_url)
        time.sleep(2)  # Wait for page to load

        # Login first
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        time.sleep(3)  # Wait for login

        # Perform logout
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_logout()
        time.sleep(3)  # Wait for logout

        # Verify Login page is displayed after logout
        login_page = LoginPage(self.driver)
        assert login_page.is_login_page_loaded(), "Login page is not loaded after logout"
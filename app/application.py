from selenium import webdriver
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.check_four_strings_bass_page import CheckFourStringsBassPage
from pages.login_page import LoginPage


class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.check_four_strings_bass_page = CheckFourStringsBassPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def quit(self):
        self.driver.quit()

    def login(self, username, password):
        self.admin_panel_login_page.open()
        self.admin_panel_login_page.enter_username(username)
        self.admin_panel_login_page.enter_password(password)
        self.admin_panel_login_page.submit_login()
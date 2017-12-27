from allure.constants import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
import allure


class AdminPanelLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.musicstore.de/ru_OT/EUR")
        return self
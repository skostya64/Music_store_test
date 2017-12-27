

class CheckFourStringsBassPage:

    def __init__(self, driver):
        self.driver = driver

    def click_menu_bass_guitars(self):
        self.driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()


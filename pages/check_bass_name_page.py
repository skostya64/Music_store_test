

class CheckBassNamePage:

    def __init__(self, driver):
        self.driver = driver

    def click_menu_bass_guitars(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.musicstore.de/ru_OT/EUR/-/cat-BASS']").click()

    def click_electric_bass_guitars(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.musicstore.de/ru_OT/EUR/-/-/cat-BASS-BASEBASS']").click()

    def click_four_strings(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.musicstore.de/ru_OT/EUR/-/4-/cat-BASS-BASEB4']").click()

    def select_name_brand(self):
        self.driver.find_element_by_xpath("//span[@class='sprite ms-checkbox']").click()





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
        self.driver.find_element_by_xpath("//span[text() = 'Производитель']").click()
        self.driver.find_element_by_xpath("//span[@title = 'Epiphone']").click()
        self.driver.find_element_by_xpath("//span[@class = 'apply btn btn-ms-std btn-lg']").click()

    def check_name_brand_in_products(self):
        for i in range(len(self.driver.find_elements_by_xpath("//div[@id = 'tile-product-BAS0008210-000']"))):
            self.driver.find_elements_by_xpath("//div[@id = 'tile-product-BAS0008210-000']")[i].click()
            brand_name = self.driver.find_element_by_xpath("//img[@title = 'Epiphone']").text
            assert brand_name == "Epiphone"


from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_main_page(self):
        driver = self.driver
        if not (len(driver.find_elements_by_name("Send e-Mail")) > 0):
            driver.get("http://localhost/addressbook")

    def return_to_main_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home").click()

    def destroy(self):
        self.driver.quit()

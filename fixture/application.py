from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_main_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")

    def return_to_main_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home").click()

    def destroy(self):
        self.driver.quit()
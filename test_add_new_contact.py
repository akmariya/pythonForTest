# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    
    def test_add_new_contact(self):
        driver = self.driver
        self.open_main_page(driver)
        self.login(driver)
        self.add_new_contact(driver, )
        self.return_to_main_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_main_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def add_new_contact(self, driver):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("ivan")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("ivanovich")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("ivanov")
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("vanya")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("some title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Some company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("some adress")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("356")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("56")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("456")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("456")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("ivan@tut.by")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("ivan2@tut.by")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("ivan3@tut.by")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("here.by")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("17")
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("2003")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("13")
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("April")
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2005")
        driver.find_element_by_name("new_group").click()
        Select(driver.find_element_by_name("new_group")).select_by_visible_text("Some Name")
        driver.find_element_by_name("new_group").click()
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("Some sdress")
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("home adrees")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Some notes")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, driver):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

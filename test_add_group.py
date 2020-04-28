# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_group(self):
        driver = self.driver
        self.open_main_page(driver)
        self.login(driver, login="admin", password="secret")
        self.add_new_group(driver, Group("Some name","Some logo", "Some comment"))
        self.open_group_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def open_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def add_new_group(self, driver, group):
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.logo)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.comment)
        driver.find_element_by_name("submit").click()

    def login(self, driver, login, password):
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, driver):
        driver.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

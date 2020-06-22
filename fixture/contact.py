from selenium.webdriver.support.ui import Select
import re
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.add_info_to_contact(contact)
        self.type_drop("new_group", contact.new_group)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_main_page()
        self.contact_cache = None

    def edit_some_contact_by_index(self, contact, index):
        driver = self.app.driver
        self.app.open_main_page()
        self.open_contact_for_edit_by_index(index)
        self.add_info_to_contact(contact)
        driver.find_element_by_name("update").click()
        self.app.return_to_main_page()
        self.contact_cache = None

    def open_contact_for_edit_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_for_view_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def add_info_to_contact(self, contact):
        driver = self.app.driver
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("homepage", contact.homepage)
        self.type_drop("bday", contact.bday)
        self.type_drop("bmonth", contact.bmonth)
        self.type_drop_year("byear", contact.byear)
        self.type_drop("aday", contact.aday)
        self.type_drop("amonth", contact.amonth)
        self.type_drop_year("ayear", contact.ayear)
        self.type("address2", contact.address2)
        self.type("phone2", contact.phone2)
        self.type("notes", contact.notes)

    def type(self,  field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def type_drop(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            Select(driver.find_element_by_name(field_name)).select_by_visible_text(text)
            driver.find_element_by_name(field_name).click()

    def type_drop_year(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)
            driver.find_element_by_name(field_name).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.app.open_main_page()
        self.select_contact_by_index(index)
        driver.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        driver.switch_to_alert().accept()
        self.app.return_to_main_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def count(self):
        driver = self.app.driver
        self.app.open_main_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_main_page()
            self.contact_cache = []
            for element in driver.find_elements_by_name("entry"):
                text = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = text[5].text
                all_emails = text[4].text
                address = text[3].text
                self.contact_cache.append(Contact(firstname=text[2].text, lastname=text[1].text, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return self.contact_cache

    def get_info_from_edit_page(self, index):
        driver = self.app.driver
        self.app.open_main_page()
        self.open_contact_for_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        phone2 = driver.find_element_by_name("phone2").get_attribute("value")
        email = driver.find_element_by_name("email").get_attribute("value")
        email2 = driver.find_element_by_name("email2").get_attribute("value")
        email3 = driver.find_element_by_name("email3").get_attribute("value")
        address = driver.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=homephone, mobile=mobilephone, work=workphone, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.app.open_main_page()
        self.open_contact_for_view_by_index(index)
        text = driver.find_element_by_id("content").text
        print(text)
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone, work=workphone, phone2=phone2)

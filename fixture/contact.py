from selenium.webdriver.support.ui import Select

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

    def edit_first_contact(self, contact, index):
        driver = self.app.driver
        self.app.open_main_page()
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.add_info_to_contact(contact)
        driver.find_element_by_name("update").click()
        self.app.return_to_main_page()
        self.contact_cache = None

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
        self.type_drop("aday", contact.bday)
        self.type_drop("amonth", contact.bmonth)
        self.type_drop_year("ayear", contact.byear)
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
                id = element.find_element_by_name("selected[]").get_attribute(
                    "value")
                self.contact_cache.append(Contact(firstname=text[2].text, lastname=text[1].text, id=id))
        return self.contact_cache

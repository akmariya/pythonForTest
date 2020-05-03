

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.logo)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.comment)
        driver.find_element_by_name("submit").click()
        self.open_group_page()

    def edit_first_group(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.logo)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.comment)
        driver.find_element_by_name("update").click()
        self.open_group_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.open_group_page()


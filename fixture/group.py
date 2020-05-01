

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.logo)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.comment)
        driver.find_element_by_name("submit").click()
        self.app.open_group_page()
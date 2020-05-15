

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("new").click()
        self.add_info_to_group(group)
        driver.find_element_by_name("submit").click()
        self.open_group_page()

    def edit_first_group(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.add_info_to_group(group)
        driver.find_element_by_name("update").click()
        self.open_group_page()

    def add_info_to_group(self, group):
        driver = self.app.driver
        self.type("group_name", group.name)
        self.type("group_header", group.logo)
        self.type("group_footer", group.comment)

    def type(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.open_group_page()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements_by_name("selected[]"))

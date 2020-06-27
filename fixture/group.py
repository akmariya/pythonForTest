from model.group import Group


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
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(group, 0)

    def edit_group_by_index(self,group, index):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_index(index)
        driver.find_element_by_name("edit").click()
        self.add_info_to_group(group)
        driver.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def edit_group_by_id(self,group, id):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_id(id)
        driver.find_element_by_name("edit").click()
        self.add_info_to_group(group)
        driver.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

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
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_index(index)
        driver.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_id(id)
        driver.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()

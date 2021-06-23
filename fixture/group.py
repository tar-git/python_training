
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select the first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def modify_group(self, number, group):
        self.modify_group_properties(number, {
            "name"   : group.name,
            "header" : group.header,
            "footer" : group.footer
        })

    def modify_group_properties(self, number, props):
        self.edit_group(number)
        for prop, new_value in props.items():
            self.send_keys_to_group_property(prop, new_value)
        self.update_group()
        self.return_to_groups_page()

    def edit_group(self, number):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath(f"//div[@id='content']/form/span[{number}]/input").click()
        wd.find_element_by_name("edit").click()

    def send_keys_to_group_property(self, prop, new_value):
        wd = self.app.wd
        wd.find_element_by_name(prop).click()
        wd.find_element_by_name(prop).clear()
        wd.find_element_by_name(prop).send_keys(new_value)

    def update_group(self):
        self.app.wd.find_element_by_name("update").click()

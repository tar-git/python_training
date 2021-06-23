class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select the first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def edit_contact(self, number):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath(f"//table[@id='maintable']/tbody/tr[{number+1}]/td[8]/a/img").click()

    def send_keys_to_contact_property(self, prop, new_value):
        wd = self.app.wd
        wd.find_element_by_name(prop).click()
        wd.find_element_by_name(prop).clear()
        wd.find_element_by_name(prop).send_keys(new_value)

    def update_contact(self):
        self.app.wd.find_element_by_name("update").click()

    def modify_contact_properties(self, number, props):
        self.edit_contact(number)
        for prop, new_value in props.items():
            self.send_keys_to_contact_property(prop, new_value)
        self.update_contact()

    def modify_contact(self, number, contact):
        self.modify_contact_properties(number, {
            "firstname"    : contact.firstname,
            "lastname"     : contact.lastname,
            "address"      : contact.address,
            "home_phone"   : contact.home_phone,
            "mobile_phone" : contact.mobile_phone,
            "email"        : contact.email
        })

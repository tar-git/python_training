import re
from selenium.webdriver.common.by import By
from fixture.common import wait_for
from model.contact import Contact
from time import sleep


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wait_for(wd, By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_css_selector('input[name="submit"][type="submit"][value="Enter"]').click()
        wait_for(wd, By.CSS_SELECTOR, 'div[class="msgbox"]')
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wait_for(self.app.wd, By.NAME, "firstname")
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wait_for(wd, By.NAME, "selected[]")
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, cid):
        wd = self.app.wd
        wait_for(wd, By.NAME, "selected[]")
        wd.find_element_by_css_selector("input[value='%s']" % cid).click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == self.app.base_url
           and len(wd.find_elements_by_link_text("Last name")) > 0):
            wait_for(wd, By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, cid):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(cid)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # open modification form
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, cid, new_contact_data):
        wd = self.app.wd
        # open modification form
        self.open_contact_to_edit_by_id(cid)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.get(wd.current_url)
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            wait_for(wd, By.CSS_SELECTOR, "tr[name=entry]")
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cid = element.find_element_by_name("selected[]").get_attribute("value")
                fields = element.find_elements_by_css_selector('td')
                firstname = fields[2].text
                lastname = fields[1].text
                address = fields[3].text
                all_emails = fields[4].text
                all_phones = fields[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, cid=cid))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath('//img[@title="Details"]')[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wait_for(wd, By.XPATH, '//img[@title="Edit"]')
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, cid):
        wd = self.app.wd
        self.app.open_home_page()
        wait_for(wd, By.CSS_SELECTOR, 'tr[name="entry"]')
        # row = wd.find_element_by_css_selector('tr[name="entry"] input[value="%s"]' % cid).parent
        # row.find_element_by_css_selector('img[title="Edit"]').click()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"] img' % cid).click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')
        cid = wd.find_element_by_name('id').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, address=address,
                       email=email, email2=email2, email3=email3,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone, cid=cid)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        m = re.search('H: (.*)', text)
        home_phone = m.group(1) if m is not None else ''
        m = re.search('M: (.*)', text)
        mobile_phone = m.group(1) if m is not None else ''
        m = re.search('W: (.*)', text)
        work_phone = m.group(1) if m is not None else ''
        m = re.search('P: (.*)', text)
        secondary_phone = m.group(1) if m is not None else ''
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)

    def add_in_group(self, group, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector('select[name="to_group"] option[value="%s"]' % group.id).click()
        wd.find_element_by_css_selector('input[value="Add to"]').click()
        self.app.open_home_page()

    def delete_from_group(self, group, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wait_for(wd, By.CSS_SELECTOR, 'select[name="group"] option[value="%s"]' % group.id).click()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector('input[type="submit"][name="remove"]').click()
        self.app.open_home_page()

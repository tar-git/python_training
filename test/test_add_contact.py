# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, orm, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Given Add new contact'):
        old_contacts = orm.get_contact_list()
    with allure.step(f'When I add a contact {contact} to the list'):
        app.contact.create(contact)
    with allure.step(f'Then the new group list is equal to the old list with the added group'):
        new_contacts = orm.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

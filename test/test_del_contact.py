# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_some_contact(app, orm, check_ui):
    old_contacts = orm.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname='test'))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

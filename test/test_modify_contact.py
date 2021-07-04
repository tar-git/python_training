# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname='test'))
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="New firstname", lastname="New lastname")
    new_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

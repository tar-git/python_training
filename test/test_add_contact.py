# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.common import random_string
import pytest


test_data = [
    Contact(firstname=firstname, lastname=lastname, address=address,
            email=email, email2=email2, email3=email3,
            home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
            secondary_phone=secondary_phone)
    for name in [random_string("name", 10)]
    for firstname in [random_string("firstname", 10)]
    for lastname in [random_string("lastname", 10)]
    for address in [random_string("address", 10)]
    for email in [random_string("email", 10)]
    for email2 in [random_string("email2", 10)]
    for email3 in [random_string("email3", 10)]
    for home_phone in [random_string("home_phone", 10)]
    for mobile_phone in [random_string("mobile_phone", 10)]
    for work_phone in [random_string("work_phone", 10)]
    for secondary_phone in [random_string("secondary_phone", 10)]
] + [Contact(
        firstname= "", lastname= "",
        address= "", email= "", email2= "",
        email3= "", home_phone= "", mobile_phone= "",
        work_phone= "", secondary_phone= ""
)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact("", "", "", "", "", "")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

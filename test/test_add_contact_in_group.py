from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name = "test"))
        group_list = orm.get_group_list()
    group = random.choice(group_list)
    contact_list = orm.get_contacts_not_in_group(group)
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname='test'))
        contact_list = orm.get_contacts_not_in_group(group)
    contact = random.choice(contact_list)
    app.contact.add_in_group(group, contact)
    assert contact in orm.get_contacts_in_group(group)

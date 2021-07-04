from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        group = app.group.create(Group(name = "test"))
        group_list = orm.get_group_list()
    else:
        group = random.choice(group_list)

    contact_list = orm.get_contact_list()
    if len(contact_list) == 0:
        contact = app.contact.create(Contact(firstname='test'))
    else:
        contact = random.choice(contact_list)

    contacts_in_groups = {i[0]: i[1] for i in filter(lambda i: len(i[1]) != 0, [
        (g, orm.get_contacts_in_group(g)) for g in group_list
    ])}
    if len(contacts_in_groups) == 0:
        app.contact.add_in_group(group, contact)
        contacts_in_groups[group] = [contact]

    group = random.choice(list(contacts_in_groups.keys()))
    contact = random.choice(contacts_in_groups[group])
    app.contact.delete_from_group(group, contact)
    assert contact not in orm.get_contacts_in_group(group)

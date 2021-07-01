import re
from random import randrange


def test_random_contact_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_hp = app.contact.get_contact_list()[index]
    contact_from_ep = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_hp.firstname == contact_from_ep.firstname
    assert contact_from_hp.lastname == contact_from_ep.lastname
    assert contact_from_hp.address == contact_from_ep.address
    assert contact_from_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_ep)
    assert contact_from_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_ep)


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                        map(lambda x: clear(x),
                            filter(lambda x: x is not None,
                                [
                                    contact.home_phone,
                                    contact.mobile_phone,
                                    contact.work_phone,
                                    contact.secondary_phone
                                ]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x!="",
    [
        contact.email,
        contact.email2,
        contact.email3
    ]))

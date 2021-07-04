import re
from model.contact import Contact


def test_contacts_on_home_page(app, orm):
    contacts_from_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    for idx in range(len(contacts_from_db)):
        contact_from_hp = contacts_from_hp[idx]
        contact_from_db = contacts_from_db[idx]
        assert contact_from_hp.firstname == contact_from_db.firstname
        assert contact_from_hp.lastname == contact_from_db.lastname
        assert contact_from_hp.address == contact_from_db.address
        assert contact_from_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


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

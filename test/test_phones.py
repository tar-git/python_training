import re


def test_phones_on_home_page(app):
    contact_from_hp = app.contact.get_contact_list()[0]
    contact_from_ep = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_ep)


def test_phones_on_contact_view_page(app):
    contact_from_vp = app.contact.get_contact_from_view_page(0)
    contact_from_ep = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_vp.home_phone == contact_from_ep.home_phone
    assert contact_from_vp.mobile_phone == contact_from_ep.mobile_phone
    assert contact_from_vp.work_phone == contact_from_ep.work_phone
    assert contact_from_vp.secondary_phone == contact_from_ep.secondary_phone


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

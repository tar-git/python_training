# -*- coding: utf-8 -*-
def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_properties(1, {'firstname': 'modified_firstname'})
    app.session.logout()


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_properties(2, {
        'firstname': 'updated_firstname',
        'lastname' : 'updated_lastname',
        'address'  : 'updated_address',
        'home'     : 'updated_home',
        'mobile'   : 'updated_mobile',
        'email'    : 'updated_email'
    })
    app.session.logout()

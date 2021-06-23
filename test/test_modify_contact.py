# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.modify_contact(1, Contact(
        'modified_firstname', 
        'modified_lastname', 
        'modified_address', 
        'modified_home', 
        'modified_mobile', 
        'modified_email'
    ))
    app.session.logout()

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    contact = Contact(u"Иван", u"Петров", u"Россия", "123", "321", "ivan@petrov.ru")
    app.contact.create(contact)


def test_add_empty_contact(app):
    app.contact.create(Contact("", "", "", "", "", ""))

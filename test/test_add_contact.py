# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    contact = Contact(u"Иван", u"Петров", u"Россия", "123", "321", "ivan@petrov.ru")
    app.contact.create(contact)
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", "", ""))
    app.session.logout()

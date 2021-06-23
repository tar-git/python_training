# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(1, Group('modified_name', 'modified_header', 'modified_footer'))
    app.session.logout()

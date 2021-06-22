# -*- coding: utf-8 -*-
def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group_properties(1, {'group_name': 'modified_group_name'})
    app.session.logout()


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group_properties(1, {
        'group_name': 'updated_group_name',
        'group_header': 'updated_group_header',
        'group_footer': 'updated_group_footer'
    })
    app.session.logout()

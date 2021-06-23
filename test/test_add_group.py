# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_group_1", header="test_group_1", footer="test_group_1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

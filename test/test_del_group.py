# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_delete_some_group(app, orm, check_ui):
    old_groups = orm.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name = "test"))
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = orm.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

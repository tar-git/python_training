# -*- coding: utf-8 -*-
from fixture.common import random_string
from model.group import Group
import pytest
import re


def clear_group_name(name):
    cleared_name = re.sub(r' {2,}', ' ', name)
    return cleared_name.strip()


test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", clear_group_name(random_string("name_", 10))]
    for header in ["", random_string("header_", 10)]
    for footer in ["", random_string("footer_", 10)]
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


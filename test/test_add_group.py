# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    old_groups = db.get_group_list()
    app.group.create(json_groups)
    assert len(old_groups) + 1 == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups.append(json_groups)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

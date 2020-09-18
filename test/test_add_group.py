# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, json_groups, check_ui):
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I add a group to the list"):
        app.group.create(json_groups)
    with allure.step("When I compare lists of groups"):
        assert len(old_groups) + 1 == len(db.get_group_list())
        new_groups = db.get_group_list()
        old_groups.append(json_groups)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

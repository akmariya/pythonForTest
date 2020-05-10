# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("Some name", "Some logo", "Some comment"))

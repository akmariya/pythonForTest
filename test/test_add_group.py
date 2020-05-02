# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group("Some name", "Some logo", "Some comment"))
    app.session.logout()

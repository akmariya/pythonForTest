# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(login="admin", password="secret")
    app.add_new_group(Group("Some name", "Some logo", "Some comment"))
    app.logout()

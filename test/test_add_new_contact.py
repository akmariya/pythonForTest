# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.add(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanua", title="Some title",
                            company="Some company", address="Adress", home="Home", mobile=375, work=546, fax=9866, email="vanua@tut.by", email2="vanua2@tut.by",
                            email3="vanua3@tut.by", homepage="vanya.com", bday="17", bmonth="January", byear="1996", aday="26", amonth="April", ayear="2000",
                            new_group="Some Name", address2="Some adress", phone2="217", notes="Some notes"))
    app.session.logout()


def test_add_new_contact_with_empty_param(app):
    app.session.login(login="admin", password="secret")
    app.contact.add(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="", email="", email2="",
                            email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                            new_group="[none]", address2="", phone2="", notes=""))
    app.session.logout()


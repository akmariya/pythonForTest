# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.add(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanua", title="Some title",
                            company="Some company", address="Adress", home="Home", mobile=375, work=546, fax=9866, email="vanua@tut.by", email2="vanua2@tut.by",
                            email3="vanua3@tut.by", homepage="vanya.com", bday="17", bmonth="January", byear="1996", aday="26", amonth="April", ayear="2000",
                            new_group="Some name", address2="Some adress", phone2="217", notes="Some notes"))


def test_add_new_contact_with_empty_param(app):
    app.contact.add(Contact())

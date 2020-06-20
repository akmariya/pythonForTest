# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanua", title="Some title",
                            company="Some company", address="Adress", home="Home", mobile=375, work=546, fax=9866, email="vanua@tut.by", email2="vanua2@tut.by",
                            email3="vanua3@tut.by", homepage="vanya.com", bday="17", bmonth="January", byear="1996", aday="26", amonth="April", ayear="2000",
                            new_group="Some name", address2="Some adress", phone2="217", notes="Some notes")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max), sorted(new_contacts, key=Contact.id_or_max)


#def test_add_new_contact_with_empty_param(app):
#    app.contact.add(Contact())

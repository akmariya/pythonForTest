# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, json_contacts, db, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.add(json_contacts)
    assert len(old_contacts) + 1 == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.append(json_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max), sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

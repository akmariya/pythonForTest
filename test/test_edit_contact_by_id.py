from model.contact import Contact
import random


def test_edit_contact_by_id(app, json_contacts, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="New Contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_some_contact_by_id(json_contacts, contact.id)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = json_contacts
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max), sorted(new_contacts, key=Contact.id_or_max)

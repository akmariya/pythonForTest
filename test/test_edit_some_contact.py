from model.contact import Contact
import random


def test_edit_some_contact(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="New Contact"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    json_contacts.id = old_contacts[index].id
    app.contact.edit_some_contact_by_index(json_contacts, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = json_contacts
    assert sorted(old_contacts, key=Contact.id_or_max), sorted(new_contacts, key=Contact.id_or_max)

from random import randrange

from model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="New Contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New name", middlename="Ivanovich", lastname="Ivanov", nickname="Vanua", title="Some title",
                            company="Some company", address="Adress", home="Home", mobile=375, work=546, fax=9866, email="vanua@tut.by", email2="vanua2@tut.by",
                            email3="vanua3@tut.by", homepage="vanya.com", bday="17", bmonth="January", byear="1996", aday="26", amonth="April", ayear="2000",
                            new_group="Some Name", address2="Some adress", phone2="217", notes="Some notes")
    contact.id = old_contacts[index].id
    app.contact.edit_some_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max), sorted(new_contacts, key=Contact.id_or_max)

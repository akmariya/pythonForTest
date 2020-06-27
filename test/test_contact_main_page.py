from model.contact import Contact


def test_contacts_on_main_page(app, db):
    db_contacts = db.get_contact_list()
    page_contacts = app.contact.get_contact_list()
    assert len(db_contacts) == len(page_contacts)
    assert sorted(db_contacts, key=Contact.id_or_max), sorted(page_contacts, key=Contact.id_or_max)

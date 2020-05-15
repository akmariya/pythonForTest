from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="New Contact"))
    app.contact.delete_first_contact()

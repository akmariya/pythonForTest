

def test_add_new_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_first_contact(name="New name")
    app.session.logout()
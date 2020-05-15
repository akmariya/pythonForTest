from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="New Contact"))
    app.contact.edit_first_contact(Contact(firstname="New name", middlename="Ivanovich", lastname="Ivanov", nickname="Vanua", title="Some title",
                            company="Some company", address="Adress", home="Home", mobile=375, work=546, fax=9866, email="vanua@tut.by", email2="vanua2@tut.by",
                            email3="vanua3@tut.by", homepage="vanya.com", bday="17", bmonth="January", byear="1996", aday="26", amonth="April", ayear="2000",
                            new_group="Some Name", address2="Some adress", phone2="217", notes="Some notes"))

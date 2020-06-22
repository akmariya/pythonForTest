from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxamount):
    return str(random.randrange(1, maxamount))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home=random_string("home", 10), mobile=random_string("mobile", 10),
            work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), bday=random_digits(32), bmonth=random_month(),
            byear=random_digits(2021), aday=random_digits(32), amonth=random_month(),
            ayear=random_digits(2021), new_group="Some name", address2=random_string("address2", 10),
            phone2=random_string("phone2", 10), notes=random_string("notes", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_some_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="New Contact"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_some_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max), sorted(new_contacts, key=Contact.id_or_max)

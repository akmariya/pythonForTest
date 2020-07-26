import re

from model.contact import Contact


def test_phones_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_all_contact_list(), key=Contact.id_or_max)
    for i in range(app.contact.count()):
        assert contacts_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contacts_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contacts_from_home_page[i].address == contact_from_db[i].address
        assert clear(contacts_from_home_page[i].all_phones_from_home_page) == merge_phones_like_on_phone_page(contact_from_db[i])
        assert clear(contacts_from_home_page[i].all_emails_from_home_page) == merge_emails_like_on_phone_page(contact_from_db[i])


def test_phones_on_contact_view_page(app, db):
    contact_from_db = sorted(db.get_all_contact_list(), key=Contact.id_or_max)
    contacts_from_view_page = list()
    for i in range(app.contact.count()):
        contacts_from_view_page.append(app.contact.get_contact_from_view_page(i))
    contacts_from_view_page = sorted(contacts_from_view_page, key=Contact.id_or_max)
    for i in range(app.contact.count()):
        contact_from_view_page = contacts_from_view_page[i]
        assert contact_from_view_page.home == contact_from_db[i].home
        assert contact_from_view_page.mobile == contact_from_db[i].mobile
        assert contact_from_view_page.work == contact_from_db[i].work
        assert contact_from_view_page.phone2 == contact_from_db[i].phone2


def clear(s):
    return re.sub(" +", "", s)


def merge_phones_like_on_phone_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_phone_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

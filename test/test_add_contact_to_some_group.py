import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_some_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="New Contact"))
    groups = orm.get_group_list()
    contact_exist = False
    for group in groups:
        if len(orm.get_contacts_not_in_group(group)) != 0:
            contact = random.choice(orm.get_contacts_not_in_group(group))
            group_for_contact = group
            contact_exist = True
            break
    if not contact_exist:
        app.contact.add(Contact(firstname="New Contact"))
        group_for_contact = random.choice(orm.get_group_list())
        contact = random.choice(orm.get_contacts_not_in_group(group_for_contact))
    app.contact.add_contact_to_group(contact, group_for_contact)
    assert contact in orm.get_contacts_in_group(group_for_contact)
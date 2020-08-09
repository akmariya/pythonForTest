import random
from model.contact import Contact
from model.group import Group


def test_delete_contact_from_some_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="New Contact"))
    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())
    if contact in orm.get_contacts_not_in_group(group):
        app.contact.add_contact_to_group(contact, group)
    app.contact.delete_contact_from_group(contact, group)
    assert contact in orm.get_contacts_not_in_group(group)

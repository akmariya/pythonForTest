import time

from model.group import Group


def test_edit_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.edit_first_group(Group("New name", "New logo", "New comment"))
    time.sleep(10)
    app.session.logout()


from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group("New name", "New logo", "New comment"))

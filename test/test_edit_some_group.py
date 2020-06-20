from random import randrange
from model.group import Group


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group("New name", "New logo", "New comment")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max), sorted(new_groups, key=Group.id_or_max)
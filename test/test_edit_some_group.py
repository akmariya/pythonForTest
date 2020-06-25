from model.group import Group
import random


def test_edit_some_group(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    json_groups.id = old_groups[index].id
    app.group.edit_group_by_index(json_groups, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = json_groups
    assert sorted(old_groups, key=Group.id_or_max), sorted(new_groups, key=Group.id_or_max)

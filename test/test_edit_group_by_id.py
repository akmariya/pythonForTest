from model.group import Group
import random


def test_edit_group_by_id(app, json_groups, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    json_groups.id = group.id
    app.group.edit_group_by_id(json_groups, group.id)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    print(old_groups)
    print(group.id)
    print(old_groups.index(group))
    old_groups[old_groups.index(group)] = json_groups
    assert sorted(old_groups, key=Group.id_or_max), sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


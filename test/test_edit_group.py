__author__ = 'lemontree'

from model.group import Group
import random

def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    group = Group(name="new_name")
    group.id = edit_group.id
    app.group.edit_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(edit_group)
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)





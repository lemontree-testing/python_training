__author__ = 'lemontree'
from model.group import Group
import random
def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="first_group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        uigrouplist = app.group.get_group_list()
        assert sorted(new_groups, key=Group.id_or_max) == sorted(uigrouplist, key=Group.id_or_max)

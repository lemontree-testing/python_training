__author__ = 'lemontree'

from model.group import Group

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    app.group.edit_first_group(Group(footer="new_footer"))

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    app.group.edit_first_group(Group(name="new_name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    app.group.edit_first_group(Group(header="new_header"))



__author__ = 'lemontree'
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    app.group.delete_first_group()

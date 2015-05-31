__author__ = 'lemontree'

from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new_name", header="new_header", footer="new_footer"))
    app.session.logout()
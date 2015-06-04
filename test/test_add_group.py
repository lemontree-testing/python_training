# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test_selenium_rec", header="test_selenium_header", footer="test_selenium_footer"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


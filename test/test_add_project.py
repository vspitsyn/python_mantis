 #-*- coding: utf-8 -*-
from model.project import Project

# #-рабочий тест, загружает данные групп из файла json,
# #-сверяет списки, загружая данные из БД
# def test_add_group(app, json_groups, db,check_ui):
#     group = json_groups
#     old_groups = db.get_group_list()
#     app.group.create(group)
#     new_groups = db.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
#     if check_ui:
#          # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
#          new_groups = map(app.group.clean_spaces, db.get_group_list())
#          assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


import  pytest
#import time, unittest
#from data.groups import testdata
#@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])
#-рабочий тест, загружает данные проектов из модуля py,
#- сверяет списки, загружая данные из бд
def test_add_project(app, data_projects,db,check_ui):
    project = data_projects
    ss = app.project.get_project_list()
    old_projects = db.get_project_list()
    #app.project.open_project_page()
    # old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    #assert sorted(old_projects, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # assert len(old_projects)+1 == app.project.count()
    new2_projects = app.project.get_project_list()
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_groups = map(app.group.clean_spaces, db.get_group_list())
         assert sorted(new_groups, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)

"""
#-рабочий тест, загружает данные групп из файла json,
#-сверяет списки, загружая данные из интерфейса
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
"""
# -*- coding: utf-8 -*-
from model.project import Project
import random

def test_delete_some_project(app,db,check_ui):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="New project 0001", status="stable", igc=False, view_status = "private", description = "Test 001"))
    old_projects  = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
    if check_ui:
        # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
        new_projects = list(map(app.project.clean_spaces, db.get_project_list()))
        assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)


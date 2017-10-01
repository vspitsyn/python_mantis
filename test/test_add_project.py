 #-*- coding: utf-8 -*-
from model.project import Project
#-рабочий тест, загружает данные проектов из модуля py,
#- сверяет списки, загружая данные из бд
def test_add_project(app, data_projects,db,check_ui):
    project = data_projects
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)
    if check_ui:
        # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
        new_projects = list(map(app.project.clean_spaces, db.get_project_list()))
        assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)

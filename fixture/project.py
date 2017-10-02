import time
from model.project import Project
from model.functions import clear_double_space
from selenium.webdriver.support.ui import Select

class ProjectHelper:
    def __init__(self,app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_xpath("//input[@value='Create New Project']"))>0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_project_page()
        #self.return_to_projects_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.fill_field_value("name", project.name)
        self.fill_select_value("status", project.status)
        if not (bool(wd.find_element_by_name("inherit_global").is_selected) == project.igc):
            wd.find_element_by_name("inherit_global").click()
        self.fill_select_value("view_state", project.view_status)
        self.fill_field_value("description", project.description)


    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            select = Select(wd.find_element_by_xpath("//select[@name='%s']"%field_name))
            select.select_by_visible_text(text)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        #wd.find_element_by_name("delete").click()
        self.open_project_page()
        self.group_cache = None

    def select_project_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href,'?project_id=%s')]"%id).click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href,'?project_id')]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            str_projects_id=wd.find_elements_by_xpath("//a[contains(@href,'?project_id')]")
            for i,element in enumerate(wd.find_elements_by_xpath("//table[3]//tr[@class='row-1' or @class='row-2']")):
                   #id = element.find_element_by_name("selected[]").get_attribute("value")
                   str_project_id = str_projects_id[i].get_attribute("href")
                   id = str_project_id[str_project_id.find('project_id') + 11:len(str_project_id)]
                   cells = element.find_elements_by_tag_name("td")
                   name = cells[0].text
                   status = cells[1].text
                   view_status = cells[3].text
                   description = cells[4].text
                   self.project_cache.append(Project(id=id, name=name, status=status, view_status=view_status, description=description))
        return list(self.project_cache)

    #ф-я возвращает объект проект с удаленными крайними проблеами и повторяющимеся пробелами в имени
    def clean_spaces(self, project):
        return Project(id = project.id, name = clear_double_space(project.name).strip(),status = project.status)


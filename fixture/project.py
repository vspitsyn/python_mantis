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
        # init group creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit group creation
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

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def edit_group_by_index(self, index,group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']"%id).click()


    # def return_to_groups_page(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            tr=wd.find_elements_by_xpath("//tr[@class='row-1' or @class='row-2']")
            aa=wd.find_elements_by_css_selector("tr[class^='row-'")
            #aaa = wd.find_elements_by_xpath("//tr[@class,'^(row-\d)'")
            for element in wd.find_elements_by_xpath_xpath("tr.row-1"):
                a=1==1
    #         for element in wd.find_elements_by_css_selector("tr.row-1"):
    #               #id = element.find_element_by_name("selected[]").get_attribute("value")
    #               cells = element.find_elements_by_tag_name("td")
    #               lastname = cells[1].text
    #               firstname = cells[2].text
    #               company_address = cells[3].text
    #               all_mail = cells[4].text
    #               all_phones = cells[5].text
    #               #all_phones = cells[5].text.splitlines()
    #               hash = lastname + firstname + cells[3].text + cells[4].text + cells[5].text
    #               self.contact_cache.append(
    #                   Contact(lastname=lastname, firstname=firstname, id=id,company_address = company_address,
    #                           all_mail_from_home_page = all_mail, all_phones_from_home_page=all_phones, hash=hash))
    #               #self.contact_cache.append(Contact(lastname = lastname, firstname = firstname, id = id, home_phone=all_phones[0], mobile_phone=all_phones[1], work_phone = all_phones[2], fax = all_phones[3], hash = hash))
    # #              self.contact_cache.append(Contact(lastname=cells[2].text, firstname=cells[1].text, id=id))
    #     return list(self.contact_cache)
            return aa

    project_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)

    #ф-я возвращает объект группа с удаленными крайними проблеами и повторяющимеся пробелами в имени
    def clean_spaces(self, group):
        return Group(id = group.id, name = clear_double_space(group.name).strip())


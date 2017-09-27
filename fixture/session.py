import time
#import model.date_time
class SessionHelper:
    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # open_home_page
        self.app.open_home_page()
        # wd.get("http://localhost:8080/addressbook")
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        #wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        #wd.find_element_by_css_selector("span.user-info").click()
        wd.find_element_by_link_text("Logout").click()

    def is_logget_in(self):
        wd = self.app.wd
        #return len(wd.find_elements_by_css_selector("ul.breadcrumb a"))> 0
        return len(wd.find_elements_by_link_text("Logout")) > 0

#ф-я возвращает имя залогированного пользователя
    def is_logget_in_as(self,username):
        wd = self.app.wd
        return self.get_logget_user() == username
        # username_text=wd.find_element_by_css_selector("ul.breadcrumb a").text
        # if (username_text.find("(") - 1)>-1:
        #     return username_text[0:username_text.find("(") - 1]
        # else:
        #     return username_text

# ф-я возвращает имя залогированного пользователя
    def get_logget_user(self):
         wd = self.app.wd
         #чтобы получить чистое имя пользователя, вырезаем скобки:
         return wd.find_element_by_css_selector("td.login-info-left span").text


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logget_in_as(username):
                return
            else:
                self.logout()
                time.sleep(1)
        self.login(username, password)

class SignupHelper:

    def __init__(self,app):
        self.app = app

    def new_user(self, username, password):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "/signup_page.php")
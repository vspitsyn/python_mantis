from telnetlib import Telnet

class JamesHelper:
    def __init__(self,app):
        self.app = app

    def ensure_user_exists(self, username, password):
        session = JamesHelper.Session("localhost", 4555, "root", "root")
        if session.is_users_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()


    class Session:
        def __init__(self, host, port, username, password):
            #тут логин и пароль - для подключения к почтовому серверу
            self.telnet = Telnet(host, port,5)
                # соединение установили
                # 5 - таймаут в сек
            self.telnet.read_until("Login id:", 5)
            self.telnet.write(username + "\n")
            self.telnet.read_until("Password:", 5)
            self.telnet.write(password + "\n")
            self.telnet.read_until("Welcome root. HELP for a list of commands", 5)

        def is_users_registered(self, username):
            self.telnet.write("verify %s\n" % username)
            res = self.telnet.expect(["exists", "does not exists"])
            return res[0] == 0

        def create_user(self, username, password):
            self.telnet.write("adduser %s %s\n" %(username, password))
            self.telnet.read_until("User %s added" % username, 5)

        def reset_password(self, username, password):
            self.telnet.write("setpassword %s %s\n" %(username, password))
            self.telnet.read_until("Password for %s reset" % username, 5)

        def quit(self):
            self.telnet.write("quit")


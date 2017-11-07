from telnetlib import Telnet

class JamesHelper:
    def __init__(self,app):
        self.app = app

    def ensure_user_exists(self, username, password):
        pass

    class Session:
        def __init__(self, host, port, username, password):
            #тут логин и пароль - для подключения к почтовому серверу
            self.telnet = Telnet(host, port,5)
                # соединение установили
                # 5 - таймаут в сек
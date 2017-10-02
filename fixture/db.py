import mysql.connector
from model.project import Project
class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, inherit_global, view_state, description from mantis_project_table")
            for row in cursor.fetchall():
                (id, name, status, igc, view_status, description) = row
                list.append(Project(id=str(id), name=name, status=self.status_db_to_str(status), igc=bool(igc),
                                    view_status = self.view_status_db_to_str(view_status), description=description))
        finally:
            cursor.close()
        return list

    def status_db_to_str(self,db):
        status_dic ={'10':'development', '30':'release', '50':'stable', '70':'obsolete'}
        return status_dic[str(db)]

    def view_status_db_to_str(self,db):
        status_dic ={'10':'public', '50':'private'}
        return status_dic[str(db)]

    def destroy(self):
        self.connection.close()

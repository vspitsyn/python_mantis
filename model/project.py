from sys import maxsize
class Project:
    def __init__(self,
                 name = None,
                 status = None,
                 igc = True,
                 view_status = None,
                 description = None,
                 id=None):
        self.name = name
        self.status = status
        self.igc = igc
        self.view_status = view_status
        self.description = description
        self.id = id

    #метод, задающий ключ для сортировки списка объектов Группа
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    # стандартный метод, определяющий вид вывода объекта на консоль
    def __repr__(self):
        return "%s:%s;%s;%s"%(self.id, self.name, self.status)

    # стандартный метод, определяющий правила сравнения объектов
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name


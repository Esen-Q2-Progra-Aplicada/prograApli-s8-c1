from ..core.pyba_logic import PybaLogic


class PersonLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getAllPersons(self):
        database = self.createDatabaseObj()
        sql = "select * from person;"
        personList = database.executeQuery(sql)
        return personList

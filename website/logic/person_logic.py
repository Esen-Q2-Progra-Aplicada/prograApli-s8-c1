from ..core.pyba_logic import PybaLogic


class PersonLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getAllPersons(self):
        database = self.createDatabaseObj()
        sql = "select * from person;"
        personList = database.executeQuery(sql)
        return personList

    def insertPerson(self, person):
        database = self.createDatabaseObj()
        sql = (
            f"insert into person "
            + f"(id, name, age) "
            + f"values(0, '{person['name']}', {person['age']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

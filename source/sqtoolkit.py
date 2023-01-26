import sqlite3 as sql

class DataBase:
    def __init__(self, file: str) -> None:
        self._db = sql.connect(file)
        self._cursor = self._db.cursor()

    def createTable(self, tableName: str, fields: tuple) -> None:
        pass

    def dropTable(self, tableName: str) -> None:
        self._cursor.execute("DROP TABLE " + tableName)

    def insertRecord(self, tableName: str, fields: tuple, values: tuple) -> None:
        self._cursor.execute("INSERT INTO " + tableName + str(fields))

    def deleteRecord(self) -> None:
        pass

    def dbQuery(self):
        pass
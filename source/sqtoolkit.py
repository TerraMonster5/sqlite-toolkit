import sqlite3 as sql

class DataBase:
    def __init__(self, file: str) -> None:
        self._db = sql.connect(file)
        self._cursor = self._db.cursor()
    
    def __del__(self) -> None:
        self._db.close()

    def createTable(self, tableName: str, fields: tuple) -> None:
        pass

    def dropTable(self, tableName: str) -> None:
        self._cursor.execute(f"DROP TABLE {tableName}")

    def insertRecord(self, tableName: str, fields: tuple, values: tuple) -> None:
        self._cursor.execute(f"INSERT INTO {tableName}{fields} VALUES {values}")

    def deleteRecord(self) -> None:
        pass

    def dbQuery(self):
        pass
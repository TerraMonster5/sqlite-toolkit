import sqlite3 as sql
from typing import Iterable, Union

class DataBase:
    def __init__(self, file: str) -> None:
        self._db = sql.connect(file)
        self._cursor = self._db.cursor()
    
    def __del__(self) -> None:
        self._db.close()

    def createTable(self, tableName: str, fields: tuple) -> None:
        fieldsStr = ",".join(fields)
        self._cursor.execute(f"CREATE TABLE {tableName}({fieldsStr})")
        self._db.commit()

    def dropTable(self, tableName: str) -> None:
        self._cursor.execute(f"DROP TABLE {tableName}")
        self._db.commit()

    def insertRecord(self, tableName: str, fields: tuple, values: tuple) -> None:
        fieldsStr, valuesStr = ",".join(fields), ','.join(f"'{x}'" for x in values)
        self._cursor.execute(f"INSERT INTO {tableName}({fieldsStr}) VALUES ({valuesStr})")
        self._db.commit()

    def deleteRecord(self, tableName: str, condition: str) -> None:
        self._cursor.execute(f"DELETE FROM {tableName} WHERE {condition}")
        self._db.commit()

    def dbQuery(self, tableName: str, fields: str="*", condition: Union[str, None]=None, reverse: bool=False) -> Iterable[tuple]:
        query = f"SELECT {fields} FROM {tableName}"
        if condition:
            query += f" WHERE {condition}"
        if reverse:
            query += f" ORDER BY DESC"
        self._cursor.execute(query)
        rows = self._cursor.fetchall()
        for row in rows:
            yield row

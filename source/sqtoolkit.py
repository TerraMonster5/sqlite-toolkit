import sqlite3 as sql
from typing import Iterable

class DataBase:
    def __init__(self, file: str) -> None:
        self._file = file

    def createTable(self, tableName: str, fields: tuple) -> None:
        db = sql.connect(self._file)
        cursor = db.cursor()

        fieldsStr = ",".join(fields)
        cursor.execute(f"CREATE TABLE {tableName}({fieldsStr})")

        db.commit()
        db.close()
    
    def createTableNotExists(self, tableName: str, fields: tuple) -> None:
        db = sql.connect(self._file)
        cursor = db.cursor()

        fieldsStr = ",".join(fields)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName}({fieldsStr})")
        
        db.commit()
        db.close()

    def dropTable(self, tableName: str) -> None:
        db = sql.connect(self._file)
        cursor = db.cursor()

        cursor.execute(f"DROP TABLE {tableName}")
        
        db.commit()
        db.close()

    def insertRecord(self, tableName: str, fields: tuple, values: tuple) -> None:
        db = sql.connect(self._file)
        cursor = db.cursor()

        fieldsStr, valuesStr = ",".join(fields), ','.join(f"'{x}'" for x in values)
        cursor.execute(f"INSERT INTO {tableName}({fieldsStr}) VALUES ({valuesStr})")
        
        db.commit()
        db.close()

    def deleteRecord(self, tableName: str, condition: str) -> None:
        db = sql.connect(self._file)
        cursor = db.cursor()

        cursor.execute(f"DELETE FROM {tableName} WHERE {condition}")
        
        db.commit()
        db.close()

    def query(self, tableName: str, fields: str="*", condition: str | None=None, reverse: bool=False) -> Iterable[tuple | str]:
        db = sql.connect(self._file)
        cursor = db.cursor()

        query = f"SELECT {fields} FROM {tableName}"
        if condition:
            query += f" WHERE {condition}"
        if reverse:
            query += f" ORDER BY DESC"
        cursor.execute(query)
        results = cursor.fetchall()

        if len(results[0]) == 1:
            results = [x[0] for x in results]

        db.close()

        for row in results:
            yield row
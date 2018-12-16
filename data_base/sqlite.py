# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def execute(self, request):
        print("request:", request)
        with self.connection:
            result = self.cursor.execute(request).fetchall()
            return result

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

    def last_insert_rowid(self):
        return list(self.execute("SELECT last_insert_rowid()"))[0][0]

# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def execute(self, cmd):
        with self.connection:
            return self.cursor.execute(cmd)

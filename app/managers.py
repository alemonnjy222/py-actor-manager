import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.__connection = sqlite3.connect("db_name")
        self.db_name = "db_name"
        self.table_name = "table_name"
    def create(self, first_name, last_name):
        self.__connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self.__connection.commit()
    def all(self):
        cursor = self.__connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(self, pk, new_first_name, new_last_name):
        self.__connection.execute(
            f"UPDATE {self.table_name} "
            " SET first_name = ?, last_name = ? "
            " WHERE id = ?",
            (new_first_name, new_last_name, pk),
        )
        self.__connection.commit()

    def delete(self, pk):
        self.__connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (pk,)
        )
        self.__connection.commit()
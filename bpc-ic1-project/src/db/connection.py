from mysql.connector import *


class Connection:
    def __init__(self, host, user, password, database):
        self.dbConnection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        self.dbConnection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.dbConnection

    def close_connection(self):
        self.dbConnection.close()

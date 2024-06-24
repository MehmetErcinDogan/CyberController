import sqlite3


class Database:
    # def __init__(self,path = ".") -> None:
    # gonna check are there any database otherwise gonna create new one
    # self.path = path+"/CyberController.db"
    # self._connection = sqlite3.connect(self.path)
    # self._cursor = self._connection.cursor()

    # self._cursor.execute("CREATE TABLE IF NOT EXIST Users(id INT PRIMARY KEY,username TEXT NOT NULL,password TEXT NOT NULL)") # password going to stored as hash
    # self._cursor.execute("CREATE TABLE IF NOT EXISTS UsersInfos(id INT PRIMARY KEY,phone INT,address TEXT,position TEXT)")
    # self._cursor.execute("CREATE TABLE IF NOT EXISTS History()")#complete

    # self._connection.commit()
    def checkUser(self, username, password):
        if username == "admin" and password == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
            return True
        else:
            return False

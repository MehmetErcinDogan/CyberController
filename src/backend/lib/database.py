import sqlite3
import glob


class Database:
    def __init__(self, path=".") -> None:
        try:
            create = True
            for i in glob.glob(path+"/*.db"):
                if i == path+"\\CyberController.db":
                    create = False
                    break

            self.path = path+"\\CyberController.db"
            self._connection = sqlite3.connect(self.path)
            self._cursor = self._connection.cursor()

            if create:
                self._cursor.execute("PRAGMA foreign_keys=ON;")
                self._cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL);")
                self._cursor.execute(
                    "CREATE TABLE IF NOT EXISTS UsersInfos(id INTEGER PRIMARY KEY AUTOINCREMENT,phone INTEGER,address TEXT,position TEXT,photo_path TEXT,FOREIGN KEY (id) REFERENCES Users(id));")
                self._cursor.execute(
                    "CREATE TABLE IF NOT EXISTS History(id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT NOT NULL,name TEXT,user_id INTEGER NOT NULL,FOREIGN KEY (user_id) REFERENCES Users(id));")
                self._cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,description TEXT NOT NULL,author_id INTEGER NOT NULL,FOREIGN KEY (author_id) REFERENCES Users(id) );")

            self._connection.commit()
        except Exception as e:
            print("Error at init process as", e)

    def checkUser(self, username: str, password: str):
        try:
            self._cursor.execute(
                "SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
            result = self._cursor.fetchall()
            if len(result) != 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error at checkUser as", e)
            return False

    def getTasks(self):
        try:
            self._cursor.execute("SELECT title,description FROM Tasks")
            return self._cursor.fetchall()
        except Exception as e:
            print("Error at getTask as", e)
            return False

    def insertTask(self, title: str, description: str, username: str, password: str):
        try:
            self._cursor.execute(
                "SELECT id FROM Users WHERE username = ? AND password = ?", (username, password))
            author_id = int(self._cursor.fetchall()[0][0])
            self._cursor.execute(
                "INSERT INTO Tasks(title,description,author_id) VALUES (?,?,?)", (title, description, author_id))
            self._connection.commit()
            return True
        except Exception as e:
            print("Error at insert task as", e)
            return False

    def deleteTask(self,title:str,desc:str,username:str,password:str):
        try:
            self._cursor.execute(
                "SELECT id FROM Users WHERE username = ? AND password = ?", (username, password))
            author_id = int(self._cursor.fetchall()[0][0])
            
            self._cursor.execute("DELETE FROM Tasks WHERE title = ? AND description = ? AND author_id = ?",(title,desc,author_id))
            self._connection.commit()
            return True
        except Exception as e:
            print("Error at delete task as",e)
            return False
        
    def getUserInfos(self, username: str, password: str):
        try:
            self._cursor.execute(
                "SELECT id FROM Users WHERE username = ? AND password = ?", (username, password))
            id = int(self._cursor.fetchall()[0][0])
            self._cursor.execute("SELECT * FROM UsersInfos WHERE id=?", (id,))
            return self._cursor.fetchall()
        except Exception as e:
            print("Error at getUserInfos as", e)
            return False

    def insertHistory(self, name, path, user_id):
        try:
            self._cursor.execute(
                "INSERT INTO History(name,path,user_id) VALUES (?,?,?)", (name, path, user_id))
            self._connection.commit()
            return True
        except Exception as e:
            print("Error at innerHistory as", e)
            return False

    def getHistory(self, username, password):
        try:
            self._cursor.execute(
                "SELECT id FROM Users WHERE username = ? AND password = ?", (username, password))
            id = int(self._cursor.fetchall()[0][0])
            self._cursor.execute(
                "SELECT * FROM History WHERE user_id = ? ", (id,))
            return self._cursor.fetchall()
        except Exception as e:
            print("Error at getHistory as", e)
            return False

    def clearHistory(self):
        try:
            self._cursor.execute("DROP TABLE History")
            self._cursor.execute(
                "CREATE TABLE IF NOT EXISTS History(id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT NOT NULL,name TEXT,user_id INTEGER NOT NULL,FOREIGN KEY (user_id) REFERENCES Users(id));")
            self._connection.commit()
        except Exception as e:
            print("Error at getHistory as", e)
            return False
    def getUserID(self,username,password):
        self._cursor.execute(
            "SELECT id FROM Users WHERE username = ? AND password = ?", (username, password))
        id = int(self._cursor.fetchall()[0][0])
        return id
    
    def __del__(self):
        self._connection.close()

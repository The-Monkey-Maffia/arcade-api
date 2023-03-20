import mysql.connector as mysql


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:

            db = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except:
            print("❌ database connection could not be made, try again later ❌")
        else:
            print("🔗 database connection made succesfully 🔗")
            return db

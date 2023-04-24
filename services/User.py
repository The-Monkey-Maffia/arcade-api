from fastapi import HTTPException
from models.User import LoginCreateInput
from mysql.connector import MySQLConnection

class User:
    def __init__(self, data: LoginCreateInput, database: MySQLConnection) -> None:
        self.data = data
        self.db = database

    def create(self):
        try:
            with self.db.cursor() as cursor:
                query = f"INSERT INTO users(`name`,`password`)VALUES(\"{self.data['user']}\", \"{self.data['password']}\");"
                cursor.execute(query)
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not create user"
            )
        else:
            raise HTTPException(
                status_code=200,
                detail="User Created successfully"
            )

    def delete(self):
        try:
            with self.db.cursor() as cursor:
                query = f"DELETE FROM `users` WHERE `name` = \"{self.data['user']}\";"
                cursor.execute(query)
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not delete user"
            )
        else:
            raise HTTPException(
                status_code=200,
                detail="User deleted successfully"
            )
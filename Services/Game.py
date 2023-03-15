from models.Game import GameData
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase

from fastapi import HTTPException

class GameClass:
    def __init__(self, data: GameData   | None, db: MySQLConnection) -> None:
        self.data = data
        self.db = db

    def Get(self):
        with self.db.cursor() as cursor:
            cursor.execute("Game_Get()")
            returnData = cursor.fetchall()
            return returnData

    def Upsert(self) -> HTTPException:
        try:
            raise HTTPException(
                status_code=200,
                details="Create a new game"
            )
        except:
            raise HTTPException(
                status_code=500,
                details="Could not create game"
            )

    def delete(self) -> HTTPException:
        try:
            raise HTTPException(
                status_code=200,
                details="Deleted game"
            )
        except:
            raise HTTPException(
                status_code=500,
                details="Could not deleted game"
            )

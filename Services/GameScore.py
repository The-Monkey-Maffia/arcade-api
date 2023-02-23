from models.GameScore import GameScore
from mysql.connector import MySQLConnection
from fastapi import HTTPException


class GameScore:

    def __init__(self, data: GameScore, db: MySQLConnection):
        self.data = data
        self.cursor = db.cursor()

    def __del__(self):
        self.cursor.Close()

    def Get(self) -> GameScore:
        # GameId
        pass

    def Upsert(self) -> HTTPException:
        try:
            self.cursor.callprocess("", self.data)
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

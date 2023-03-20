from models.Game import GameDataInput, GameDataOutput
from mysql.connector import MySQLConnection

from fastapi import HTTPException

class GameClass:
    def __init__(self, data: GameDataInput, db: MySQLConnection) -> None:
        self.data = data
        self.db = db

    def Get(self) -> HTTPException | GameDataOutput:
        try:
            with self.db.cursor() as cursor:
                query = f"CALL game_get({self.data['id']},{self.data['gameName']},{self.data['gameAuthors']})"
                cursor.execute(query)
                returnData = cursor.fetchall()
                return returnData

        except:
            raise HTTPException(
                status_code=500,
                detail="Could not get the game data"
            )


    def Upsert(self) -> HTTPException:
        try:
            raise HTTPException(
                status_code=200,
                detail="Create a new game"
            )
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not create game"
            )

    def delete(self) -> HTTPException:
        try:
            with self.db.cursor() as cursor:
                query = (f"CALL game_delete({self.data['id']},{self.data['gameName']})")
                print(query)
                cursor.execute(query)
                self.db.commit()
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not deleted game"
            )
        else:
            raise HTTPException(
                status_code=200,
                detail="Deleted game"
            )

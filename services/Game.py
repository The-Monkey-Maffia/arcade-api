from services.Functions import tupleToDict
from models.Game import GameDataInput, GameDataOutput
from mysql.connector import MySQLConnection

from fastapi import HTTPException

class Game:
    def __init__(self, data: GameDataInput, db: MySQLConnection) -> None:
        self.data = data
        self.db = db

    def Get(self) -> HTTPException | GameDataOutput:
        try:
            with self.db.cursor() as cursor:
                query = f"CALL game_get({self.data['id']},{self.data['gameName']},{self.data['gameAuthors']})"
                cursor.execute(query)
                resultRaw = cursor.fetchall()[0]
                resultNames = ['gameId', 'gameName', 'gameAuthors', 'gameDataCreation', 'gameDateUpdate']
                filterdResult = tupleToDict(resultRaw, resultNames)
                return filterdResult

        except:
            raise HTTPException(
                status_code=500,
                detail="Could not get the game data"
            )

    def Create(self) -> HTTPException:
        try:
            with self.db.cursor() as cursor:
                query = f"CALL game_create(\"{self.data['gameName']}\",\"{self.data['gameAuthors']}\")"
                cursor.execute(query)
                self.db.commit()
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not create game"
            )
        else:
            raise HTTPException(
                status_code=200,
                detail="Created a new game"
            )


    def Delete(self) -> HTTPException:
        try:
            with self.db.cursor() as cursor:
                query = (f"CALL game_delete({self.data['id']})")
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

    def Update(self) -> HTTPException:
        try:
            with self.db.cursor() as cursor:
                query = f"CALL game_update({self.data['id']}, \"{self.data['gameName']}\", \"{self.data['gameAuthors']}\")"
                cursor.execute(query)
                self.db.commit()
        except:
            raise HTTPException(
                status_code=500,
                detail="Game could not be updated"
            )
        else:
            raise HTTPException(
                status_code=200,
                detail="Game is updated"
            )
from models.Game import GameData
from mysql.connector.cursor import CursorBase
from fastapi import HTTPException


class Game:

    def __init__(self, data: GameData, cursor: CursorBase):
        self.data = data
        self.cursor = cursor

    def Get(self) -> GameData:
        pass

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

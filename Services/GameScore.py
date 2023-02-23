from models.GameScore import GameScore
from mysql.connector.cursor import CursorBase
from fastapi import HTTPException


class GameScore:

    def __init__(self, data: GameScore, cursor: CursorBase, GameId: int):
        self.data = data
        self.cursor = cursor

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

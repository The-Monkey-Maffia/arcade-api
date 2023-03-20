from datetime import datetime
from pydantic import BaseModel


class GameDataInput(BaseModel):
    id: int
    gameName: str
    gameAuthors: datetime

class GameDataOutput(GameDataInput):
    gameDateCreated: str
    gameDataUpdated: str


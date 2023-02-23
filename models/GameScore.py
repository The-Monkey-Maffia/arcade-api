from datetime import datetime
from pydantic import BaseModel


class GameScore(BaseModel):
    Id: int | None
    GameId: str
    Score: float
    User: str
    Date: datetime

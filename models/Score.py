from datetime import datetime
from pydantic import BaseModel


class ScoreCreateInput(BaseModel):
    scoreUser: str
    score: int
    gameId: int

class ScoreGetInput(BaseModel):
    gameId: int
    scoreUser: str
    limit: int


class ScoreOutput(ScoreCreateInput):
    scoreId: int
    scoreDate: datetime



from pydantic import BaseModel


class GameScore(BaseModel):
    Id: int | None
    GameName: str
    CreateBy: str

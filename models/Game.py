from datetime import datetime
from pydantic import BaseModel


class GameData(BaseModel):
    Id: int | None
    GameName: str
    CreateBy: str
    Create: datetime

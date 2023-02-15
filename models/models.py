from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Data(BaseModel):
    Value: str

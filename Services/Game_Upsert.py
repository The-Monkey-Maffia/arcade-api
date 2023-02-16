from ..models.models import Data
from mysql.connector import cursor


def AddGame(data: Data, cursor: cursor.CursorBase):
    cursor.callproc("NameSP", data)

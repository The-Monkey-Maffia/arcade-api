
from mysql.connector import cursor


def Game_GetById(GameId: int) -> list:
    cursor.callproc('GetGame', [GameId])
    return cursor.fetchall()


def Game_Get():
    cursor.callproc('GetGame')
    return cursor.fetchall()

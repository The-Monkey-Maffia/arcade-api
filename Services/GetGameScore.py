from mysql.connector import MySQLConnection
import array


def GetGameScore(mysql: MySQLConnection) -> array:
    cursor = mysql.cursor()
    cursor.callproc('Game_Get')
    print(cursor.fetchone())
    cursor.close()
    return []
    # return cursor.fetchall()


# def GetGameScoreById(GameId: int, cursor: cursor.CursorBase) -> array:
#     cursor.callproc('GetGameDataById', [GameId])
#     return cursor.fetchall()

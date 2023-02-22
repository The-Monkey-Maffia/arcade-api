from models.GameScore import GameData
from mysql.connector import cursor
from mysql.connector import MySQLConnection


def AddGame(data: GameData, mysql: MySQLConnection) -> None:
    try:
        cursor = mysql.cursor()
        cursor.callproc("call Game_Upsert", data.Id,
                        data.GameName, data.CreateBy)
        print(cursor.fetchone())
        cursor.close()
    except:
        print("game could not be made")
    else:
        print("game made succesfully")

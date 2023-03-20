from models.GameScore import GameScore
from mysql.connector import MySQLConnection
from fastapi import HTTPException


class GameScore:

    def __init__(self, data: GameScore, db: MySQLConnection) -> None:
        self.data = data
        self.db = db
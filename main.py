from fastapi import FastAPI
from Services.Functions import tupleToDict
from config.database import Database
import os
from dotenv import load_dotenv
from Services import Game
from models.Game import GameDataInput
# from Services.AddGameData import AddGameData

app = FastAPI()
load_dotenv()
db = Database(
    os.getenv("DB_HOST"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASS"),
    os.getenv("DB_NAME")
).connect()


@app.get("/GameGet/{gameId}")
def GameGet(gameId: int, gameName: str = 0, gameAuthors: str = 0):
    gameData: GameDataInput = {'id': gameId, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game.GameClass(gameData, db)
    resultArray = game.Get()[0]
    resultNames = ['id', 'gameName', 'gameAuthors', 'gameDataCreation', 'gameDateUpdate']
    return tupleToDict(resultArray, resultNames)

@app.get("/GameDelete")
def GameDelete(gameId: int = 0, gameName: str = 0):
    gameData: GameDataInput  = {'id': gameId, 'gameName': gameName}
    game = Game.GameClass(gameData, db)
    game.delete()


# @app.get("/GetDataFromDatabase")
# def GetDataById():
#     return GetGameData(None)


# @app.post("/AddDataToDatabase")
# def AddData(data: Data):
#     return AddGameData(data, curser)

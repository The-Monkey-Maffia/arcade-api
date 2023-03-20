from fastapi import FastAPI
from Services.Functions import tupleToDict
from config.database import Database
import os
from dotenv import load_dotenv
from Services.Game import GameClass as Game
from models.Game import GameDataInput

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
    game = Game(gameData, db)
    resultArray = game.Get()[0]
    resultNames = ['id', 'gameName', 'gameAuthors', 'gameDataCreation', 'gameDateUpdate']
    return tupleToDict(resultArray, resultNames)

@app.delete("/GameDelete{gameId}")
def GameDelete(gameId: int):
    gameData: GameDataInput  = {'id': gameId}
    game = Game(gameData, db)
    game.Delete()

@app.post("/GameCreate/{gameName}")
def GameCreate(gameName: str, gameAuthors: str = None):
    gameData = {'id': 0, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game(gameData, db)
    game.Create()


@app.patch("/GameUpdate/{gameId}")
def GameUpdate(gameId: int, gameName: str = None, gameAuthors: str = None):
    gameData = {'id': gameId, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game(gameData, db)
    game.Update()
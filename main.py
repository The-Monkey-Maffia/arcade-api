from fastapi import FastAPI
from services.Functions import tupleToDict
from services.Score import Score
from config.database import Database
import os
from dotenv import load_dotenv
from services.Game import Game
from models.Game import GameDataInput

app = FastAPI()

load_dotenv()

db = Database(
    os.getenv("DB_HOST"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASS"),
    os.getenv("DB_NAME")
).connect()


@app.get("/game/get/{gameId}")
def GameGet(gameId: int, gameName: str = 0, gameAuthors: str = 0):
    gameData: GameDataInput = {'id': gameId, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game(gameData, db)
    result = game.Get()
    return result

@app.delete("/game/delete/{gameId}")
def GameDelete(gameId: int):
    gameData: GameDataInput  = {'id': gameId}
    game = Game(gameData, db)
    game.Delete()

@app.post("/game/create/{gameName}")
def GameCreate(gameName: str, gameAuthors: str = None):
    gameData = {'id': 0, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game(gameData, db)
    game.Create()

@app.patch("/game/update/{gameId}")
def GameUpdate(gameId: int, gameName: str = None, gameAuthors: str = None):
    gameData = {'id': gameId, 'gameName': gameName, 'gameAuthors': gameAuthors}
    game = Game(gameData, db)
    game.Update()

@app.get('/score/get/{gameId}')
def GetGameScore(gameId: int, scoreUser: str, outputLimit: int):
    scoreData = {'gameId': gameId, 'scoreUser': scoreUser, 'outputLimit': outputLimit}
    score = Score(scoreData, db)
    result = score.Get()
    return result

@app.post('/score/create/{score}')
def ScoreCreate(scoreValue: int, gameId: int, scoreUser: str):
    scoreData = {'gameId': gameId, 'score': scoreValue, 'scoreUser': scoreUser}
    score = Score(scoreData, db)
    score.Create()


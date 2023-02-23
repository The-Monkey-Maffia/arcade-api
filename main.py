from fastapi import FastAPI
from config.database import Database
import os
from dotenv import load_dotenv
from Services import GameScore, Game
# from Services.AddGameData import AddGameData

app = FastAPI()
load_dotenv()
db = Database(
    os.getenv("DB_HOST"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASS"),
    os.getenv("DB_NAME")
).connect()


@app.get("/GetGame")
async def GetData():
    d = Game.GameClass(None, db)
    return d.Get()


# @app.post("/AddGame/{Data}")
# def AddGameByData(Data):

#     return AddGame(Data, mydb)

# @app.get("/GetDataFromDatabase")
# def GetDataById():
#     return GetGameData(None)


# @app.post("/AddDataToDatabase")
# def AddData(data: Data):
#     return AddGameData(data, curser)

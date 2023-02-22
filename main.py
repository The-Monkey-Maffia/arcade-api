from fastapi import FastAPI
from config.database import mydb
# from Services.AddGameData import AddGameData
from Services.GetGameScore import GetGameScore
from Services.Game_Upsert import AddGame
from schemas.schemas import Data
app = FastAPI()


@app.get("/GetGameScore/{GameId}")
def GetDataById(GameId: int):
    return Data(GetGameScore(mydb))

@app.post("/AddGame/{Data}")
def AddGameByData(Data):
    return AddGame(Data, mydb)

# @app.get("/GetDataFromDatabase")
# def GetDataById():
#     return GetGameData(None)


# @app.post("/AddDataToDatabase")
# def AddData(data: Data):
#     return AddGameData(data, curser)

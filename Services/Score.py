from Services.Functions import tupleToDict
from models.Score import ScoreCreateInput, ScoreGetInput, ScoreOutput
from mysql.connector import MySQLConnection
from fastapi import HTTPException


class Score:

    def __init__(self, data: ScoreCreateInput | ScoreGetInput, db: MySQLConnection) -> None:
        self.data = data
        self.db = db

    def Get(self) -> ScoreOutput:
        try:
            with self.db.cursor() as cursor:
                query = f"CALL score_get({self.data['gameId']}, \"{self.data['scoreUser']}\", {self.data['outputLimit']})"
                cursor.execute(query)
                resultsRaw = cursor.fetchall()
                resultNames = ['scoreId', 'scoreName', 'scoreDate', 'score', 'gameId']
                results = list()
                for result in resultsRaw:
                    filterdResult = tupleToDict(result, resultNames)
                    results.append(filterdResult)
                return results
        except:
            raise HTTPException(
                status_code=500,
                detail="Could not get the score data"
            )

    def Create(self) -> HTTPException:
        pass
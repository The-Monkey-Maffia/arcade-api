def SMGameData(data: list):
    if len(data) == None:
        return []
    else:
        return {
            "Id": data[0],
            "GameName": data[1],
        }

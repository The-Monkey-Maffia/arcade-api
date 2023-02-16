import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os
dotenv_path = Path('.env')

load_dotenv(dotenv_path=dotenv_path)
print(os.getenv('IP'))
mydb = mysql.connector.connect(
    host="10.252.69.186",
    user="toor",
    password="RootRoot123",
    database="gamedatabase"
)

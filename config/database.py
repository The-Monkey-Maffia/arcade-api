import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()


mydb = mysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    database=os.environ.get("DB_NAME")
)

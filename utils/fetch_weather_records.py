from utils.mysql_connect import mysql_connect
import pandas as pd

def fetch_weather_records():
    connection = mysql_connect()
    if connection.is_connected():
        cursor = connection.cursor()
        query = "SELECT * FROM weather_records"

        cursor.execute(query)
        rows = cursor.fetchall()
        columns = ["a","b","c"]
        # df = pd.DataFrame(rows, columns)

        print(rows)

        connection.close()


fetch_weather_records()

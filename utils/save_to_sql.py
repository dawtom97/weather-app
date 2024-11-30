from utils.mysql_connect import mysql_connect

def save_to_sql(data):
    connection = mysql_connect()
    if connection.is_connected():
        cursor = connection.cursor()
        query = """
            INSERT INTO weather_records (temp,feels_like,clouds,pressure,humidity,wind_speed,description,timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (tuple(data.values()))
        )
        connection.commit()
        connection.close()

from utils.mysql_connect import mysql_connect


def create_table():
    connection = mysql_connect()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                temp FLOAT NOT NULL,
                feels_like FLOAT NOT NULL,
                clouds INT NOT NULL,
                pressure INT NOT NULL,
                humidity INT NOT NULL,
                wind_speed FLOAT NOT NULL,
                description VARCHAR(100) NOT NULL,
                timestamp DATETIME NOT NULL
            )
        """)
        connection.close()

import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="ai_recruitment"
    )

    return connection
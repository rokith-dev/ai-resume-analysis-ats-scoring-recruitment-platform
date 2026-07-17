import mysql.connector


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root123",
    "database": "ai_recruitment"
}


def get_connection():
    """
    Create and return a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print("Database Connection Error:", error)

    return None
from database.db_config import get_connection

connection = get_connection()

if connection:

    print("✅ Database Connected Successfully!")

    connection.close()

else:

    print("❌ Database Connection Failed!")
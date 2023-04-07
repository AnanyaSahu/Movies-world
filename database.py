import pyodbc

try:
    # if u have used window authentication for local running DB
    dbConnection = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-PG8J0ME5\SQLEXPRESS;'
                                  'Database=Movie db;'
                                  'Trusted_Connection=yes;')

    if True:
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * from Booking;")

        record = cursor.fetchall()

        print(record)

except Exception as e:
    print("Error while connecting to DB", e)

finally:
    # if dbConnection.is_connected():
    cursor.close()
    dbConnection.close()
    print("db connection closed")

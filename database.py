import pyodbc

try:
    # if u have used window authentication for local running DB
    dbConnection = pyodbc.connect('Driver={SQL Server};'
                      'Server=<server-name>;'
                      'Database=<table_name>;'
                      'Trusted_Connection=yes;')

    if True:
        cursor = dbConnection.cursor()

        cursor.execute("SELECT * from tableName;")

        record = cursor.fetchall()

        print( record)

except Exception as e:
    print("Error while connecting to DB", e)

finally:
    # if dbConnection.is_connected():
        cursor.close()
        dbConnection.close()
        print("db connection closed")

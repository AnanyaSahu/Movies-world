import pyodbc

global dbConnection
global cursor


# connect to database
def openDbConnection():
    try:
        dbConnection = pyodbc.connect('Driver={SQL Server};'
                                      'Server=ANNA\MSSQLSERVER03;'
                                      'Database=Travel DB;'
                                      'Trusted_Connection=yes;')

        if dbConnection.getinfo != None:
            cursor = dbConnection.cursor()
        return cursor

    except Exception as e:
        print("Error while connecting to DB", e)

# close datbase connection


def closeDbConnection():
    if dbConnection.getinfo != None:
        cursor.close()
        dbConnection.close()
        print("db connection closed")

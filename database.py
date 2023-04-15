import pyodbc

global dbConnection
global cursor


class databaseConnection:
    def __init__(self):
        pass

# connect to database
    def openDbConnection(self):
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


    def closeDbConnection(self):
        if dbConnection.getinfo != None:
            cursor.close()
            dbConnection.close()
            print("db connection closed")

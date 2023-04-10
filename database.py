import pyodbc

global dbConnection
global cursor


# try:
#     dbConnection = pyodbc.connect('Driver={SQL Server};'
#                       'Server=ANNA\MSSQLSERVER03;'
#                       'Database=Travel DB;'
#                       'Trusted_Connection=yes;')

#     if True:
#         cursor = dbConnection.cursor()
#         cursor.execute("SELECT [adminId],[adminName] FROM [Travel DB].[dbo].[Admin];")

#         record = cursor.fetchall()

#         print( record)

# except Exception as e:
#     print("Error while connecting to DB", e)

# finally:
#     # if dbConnection.is_connected():


def openDbConnection():
    try:
        dbConnection = pyodbc.connect('Driver={SQL Server};'
                      'Server=ANNA\MSSQLSERVER03;'
                      'Database=Travel DB;'
                      'Trusted_Connection=yes;')

        if dbConnection.getinfo != None:
            cursor = dbConnection.cursor()
            # cursor.execute("SELECT [adminId],[adminName] FROM [Travel DB].[dbo].[Admin];")

            # record = cursor.fetchall()

        # print( record)
        return cursor

    except Exception as e:
        print("Error while connecting to DB", e)



def closeDbConnection():
        if dbConnection.getinfo != None:
            cursor.close()
            dbConnection.close()
            print("db connection closed")
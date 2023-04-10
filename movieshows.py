from database import openDbConnection

def  getAreas():
    cursor = openDbConnection()
    getAreaQuery = "SELECT *FROM  [movieDb].[dbo].[Area];" 
    record = cursor.execute(getAreaQuery)
    print(record.fetchall())
    r= [tuple(row) for row in record]
    return {'rows': r}



def getTheaters(area):
    # sort closest to farthgest from ara
    return {'rows': []}
    
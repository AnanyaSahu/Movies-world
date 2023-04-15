from database import databaseConnection

class movieTheater:
    def __init__(self):
        pass
    # This methyod will get the list of area
    def  getAreas(self):
        d = databaseConnection()
        cursor = d.openDbConnection()
        getAreaQuery = "SELECT *FROM  [movieDb].[dbo].[Area];" 
        record = cursor.execute(getAreaQuery).fetchall()
        print(record)
        r= [tuple(row) for row in record]
        print(r)
        return {'rows': r}


    # Method to Obtain details of nearby theatres and sort them based on their distance from the area's location
    def get_nearby_theaters(self,area):
        d = databaseConnection()
        cursor = d.openDbConnection()
        getNearByTheaterQuery = "SELECT t.thearerName, t.theaterId, a.areaId, a.areaName, abs(a.location-"+str(area)+"), t.rowRange, t.ColumnRange FROM [movieDb].[dbo].[Theater] t Inner join [movieDb].[dbo].Area a ON t.areaId = a.areaId group by t.thearerName, t.theaterId, a.areaId, a.areaName,abs(a.location-"+str(area)+"), t.rowRange, t.ColumnRange  order by abs(a.location-"+str(area)+");" 
        print(getNearByTheaterQuery)
        record = cursor.execute(getNearByTheaterQuery).fetchall()
        r= [tuple(row) for row in record]
        print(r)
        return {'rows': r}


from database import openDbConnection

conn = sqlite3.connect('theatres.db')
c = conn.cursor()

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
    
    
    


def get_movies_by_theatre(theatre):
    c.execute("SELECT movie_title FROM movies WHERE theatre_name = ?", (theatre,))
    return [row[0] for row in c.fetchall()]

print("Select a theatre:")
c.execute("SELECT DISTINCT theatre_name FROM movies")
for row in c.fetchall():
    print(row[0])
selected_theatre = input("> ")

print(f"Movies playing at {selected_theatre}:")
for movie in get_movies_by_theatre(selected_theatre):
    print(movie)

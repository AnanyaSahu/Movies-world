from database import openDbConnection

# this method is used to get the list of movies from the selected theater
def get_movies_by_theatre(theatreId):
    cursor = openDbConnection()
    getMovieByTheaterQuery = "SELECT tm.id, tm.theaterId ,tm.movieId, m.movieName, m.showTiming, m.duration, m.ageConstraint FROM [movieDb].[dbo].[TheaterMovie] tm INNER JOIN [movieDb].[dbo].[Movie] m  on tm.movieId = m.movieId where tm.theaterId = "+ str(theatreId) 
    print(getMovieByTheaterQuery)
    record = cursor.execute(getMovieByTheaterQuery).fetchall()
    print(record)
    r= [tuple(row) for row in record]
    return {'rows': r}

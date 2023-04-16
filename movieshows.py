from database import databaseConnection


class getMovieShow:
  def __init__(self):
    pass
      # this method is used to get the list of movies from the selected theater
  def get_movies_by_theatre(self,theatreId):
    d = databaseConnection()
    cursor = d.openDbConnection()
    getMovieByTheaterQuery = "SELECT tm.id, tm.theaterId ,tm.movieId, m.movieName, m.showTiming, m.duration, m.ageConstraint FROM [MoviesWorld].[dbo].[TheaterMovie] tm INNER JOIN [MoviesWorld].[dbo].[Movie] m  on tm.movieId = m.movieId where tm.theaterId = "+ str(theatreId) 
    record = cursor.execute(getMovieByTheaterQuery).fetchall()
    r= [tuple(row) for row in record]
    return {'rows': r}


     

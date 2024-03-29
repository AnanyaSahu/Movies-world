# Baran Azak
# commited changes
from database import databaseConnection

class createTicketsForBookings:
    def __init__(self):
        pass

    def createTicket(self,booking_id):
        d = databaseConnection()
        cursor = d.openDbConnection()

        getBookedTicketsrQuery = "SELECT t.theaterId , t.thearerName, a.areaName, b.customerName, m.movieName, m.showTiming, b.seatBooked FROM [MoviesWorld].[dbo].[Booking] b INNER JOIN [MoviesWorld].[dbo].[Theater] t ON b.theraterId = t.theaterId INNER JOIN [MoviesWorld].[dbo].[Area] a ON t.areaId = a.areaId INNER JOIN [MoviesWorld].[dbo].[Movie] m ON b.movieId = m.movieId WHERE b.bookingId = " + str(
            booking_id)
        results = cursor.execute(getBookedTicketsrQuery).fetchall()
        r= [tuple(row) for row in results]
        return {'rows': r}

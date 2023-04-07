# Baran Azak
import pyodbc

try:
    # if u have used window authentication for local running DB
    dbConnection = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-PG8J0ME5\SQLEXPRESS;'
                                  'Database=Movie db;'
                                  'Trusted_Connection=yes;')

    if True:
        cursor = dbConnection.cursor()
        # Set booking ID to fetch
        booking_id = 102
        # Execute query with booking ID parameter
        cursor.execute("""
            SELECT Theater.thearerName, Area.areaName, Booking.customerName, Movie.movieName, Movie.showTiming, Booking.seatBooked
            FROM Booking
            INNER JOIN Theater ON Booking.theraterId = Theater.theaterId
            INNER JOIN Area ON Theater.areaId = Area.areaId
            INNER JOIN Movie ON Booking.movieId = Movie.movieId
            WHERE Booking.bookingId = ?
            """, (booking_id,))
        # Fetch results
        result = cursor.fetchone()

        # Print booking details
        print("Theater Name:", result[0])
        print("Theater Area:", result[1])
        print("Customer Name:", result[2])
        print("Movie Name:", result[3])
        print("Show Timing:", result[4])
        print("Booked Seats:", result[5])


except Exception as e:
    print("Error while connecting to DB", e)

finally:
    cursor.close()
    dbConnection.close()
    print("db connection closed")

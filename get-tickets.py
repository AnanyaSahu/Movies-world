# Baran Azak
# commited changes
import pyodbc
import requests


# def download_database_file():
#    url = 'https://example.com/'
#    response = requests.get(url)
#    with open('LAPTOP-PG8J0ME5\SQLEXPRESS', 'wb') as f:
#        f.write(response.content)
#    print('Database file downloaded !')


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
        results = cursor.fetchall()

except Exception as e:
    print("Error while connecting to DB", e)

# Closing DB
finally:
    cursor.close()
    dbConnection.close()
    print("db connection closed")

    # Write the results to a file
    with open('bookingdetails.txt', 'w') as f:
        for theater_name, area_name, customer_name, movie_name, show_timing, seat_booked in results:
            f.write("The booking details for booking ID {} are:\n".format(booking_id))
            f.write("Theater Name: {}\n".format(theater_name))
            f.write("Theater Area: {}\n".format(area_name))
            f.write("Customer Name: {}\n".format(customer_name))
            f.write("Movie Name: {}\n".format(movie_name))
            f.write("Show Timing: {}\n".format(show_timing))
            f.write("Booked Seats: {}\n".format(seat_booked))
            f.write("\n")

    url = 'file:///C:/Users/baran/OneDrive/Masa%C3%BCst%C3%BC/Python%20Project/bookingdetails.txt'
    response = requests.get(url)
    with open('bookingdetails.txt', 'w') as f:
        f.write(response.text)
    print('Text file downloaded.')

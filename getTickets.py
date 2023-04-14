# Baran Azak
# commited changes
import pyodbc
import requests
from database import openDbConnection


def createTicket(booking_id):
    cursor = openDbConnection()

    getTherterQuery = "SELECT t.thearerName, a.areaName, b.customerName, m.movieName, m.showTiming, b.seatBooked FROM [movieDb].[dbo].[Booking] b INNER JOIN [movieDb].[dbo].[Theater] t ON b.theraterId = t.theaterId INNER JOIN [movieDb].[dbo].[Area] a ON t.areaId = a.areaId INNER JOIN [movieDb].[dbo].[Movie] m ON b.movieId = m.movieId WHERE b.bookingId = " + str(
        booking_id)
    print(getTherterQuery)
    results = cursor.execute(getTherterQuery).fetchall()
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

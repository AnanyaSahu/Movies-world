# Baran Azak
# commited changes
from database import databaseConnection
from pathlib import Path
import os
from flask import Flask, send_file


class createTicketsForBookings:
    def _init_(self):
        pass

    def createTicket(self,booking_id):
        d = databaseConnection()
        cursor = d.openDbConnection()

        getTherterQuery = "SELECT t.theaterId , t.thearerName, a.areaName, b.customerName, m.movieName, m.showTiming, b.seatBooked FROM [movieDb].[dbo].[Booking] b INNER JOIN [movieDb].[dbo].[Theater] t ON b.theraterId = t.theaterId INNER JOIN [movieDb].[dbo].[Area] a ON t.areaId = a.areaId INNER JOIN [movieDb].[dbo].[Movie] m ON b.movieId = m.movieId WHERE b.bookingId = " + str(
            booking_id)
        print(getTherterQuery)
        results = cursor.execute(getTherterQuery).fetchall()
        r= [tuple(row) for row in results]
        # with open('bookingdetails.txt', 'w') as f:
            # for theater_name, area_name, customer_name, movie_name, show_timing, seat_booked in results:
                # f.write("The booking details for booking ID {} are:\n".format(results[0][0]))
                # f.write("Theater Name: {}\n".format(results[0][1]))
                # f.write("Theater Area: {}\n".format(results[0][2]))
                # f.write("Customer Name: {}\n".format(results[0][3]))
                # f.write("Movie Name: {}\n".format(results[0][4]))
                # f.write("Show Timing: {}\n".format(results[0][5]))
                # f.write("Booked Seats: {}\n".format(results[0][6]))
                # f.write("\n")
        return {'rows': r}

        # url = './bookingdetails.txt'
        # response = requests.get(url)

        # # # with open('./bookingdetails.txt', 'w') as f:
        # # #     f.write(response.text)
        # filename = Path('bookingdetails.txt')
        # print(filename)
        # open(filename, 'wb').write(bookingdetails.c)
        
        # print('Text file downloaded.')

    # def downlaodTicket(booking_id):
    #     cursor = openDbConnection()

    #     getTherterQuery = "SELECT t.theaterId , t.thearerName, a.areaName, b.customerName, m.movieName, m.showTiming, b.seatBooked FROM [movieDb].[dbo].[Booking] b INNER JOIN [movieDb].[dbo].[Theater] t ON b.theraterId = t.theaterId INNER JOIN [movieDb].[dbo].[Area] a ON t.areaId = a.areaId INNER JOIN [movieDb].[dbo].[Movie] m ON b.movieId = m.movieId WHERE b.bookingId = " + str(
    #         booking_id)
    #     results = cursor.execute(getTherterQuery).fetchall()
    #     r= [tuple(row) for row in results]
    #     with open('bookingdetails.txt', 'w') as f:
    #             f.write("The booking details for booking ID {} are:\n".format(results[0][0]))
    #             f.write("Theater Name: {}\n".format(results[0][1]))
    #             f.write("Theater Area: {}\n".format(results[0][2]))
    #             f.write("Customer Name: {}\n".format(results[0][3]))
    #             f.write("Movie Name: {}\n".format(results[0][4]))
    #             f.write("Show Timing: {}\n".format(results[0][5]))
    #             f.write("Booked Seats: {}\n".format(results[0][6]))
    #             f.write("\n")
    

    #     filepath = os.path.join(os.getcwd(), 'bookingdetails.txt')

    #     # Download the file
    #     return send_file(filepath, as_attachment=True)


    # downlaodTicket(168)

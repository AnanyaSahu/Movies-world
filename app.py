from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from booktickets import getBookingsForCustomer as getBookingsForCustomerFromBooking, cancelUserBooking,updateCustomerName,showSeats, bookTickets
from movietheaters import getAreas
from movietheaters import get_nearby_theaters
from movieshows import get_movies_by_theatre
from getTickets import createTicket

mysql = MySQL()
app = Flask(__name__)
CORS(app)
# # My SQL Instance configurations
# # Change the HOST IP and Password to match your instance configurations
# app.config['MYSQL_USER'] = 'web'
# app.config['MYSQL_PASSWORD'] = 'webPass'
# app.config['MYSQL_DB'] = 'student'
# app.config['MYSQL_HOST'] = 'localhost' #for now
mysql.init_app(app)



# This method will get booking deatails for a customer, input is customer name
@app.route('/getBookingsForCustomer/<name>', methods=['GET'])
def  getBookingsForCustomer(name):
    return getBookingsForCustomerFromBooking(name)

# This method will list all the area
@app.route('/getAreaList/', methods=['GET'])
def  getAreaList():
    return getAreas()
    
# This method will list all the theaters ans return a list of theaters ordered by the nearest to farthest area, input is areacode 
@app.route('/getTheratersList/<area>', methods=['GET'])
def  getListTheraters(area):
    return get_nearby_theaters(area)

# This method will list all the movies for the selacted theater, input is theater id
@app.route('/getMovieList/<theaterId>', methods=['GET'])
def  getMovieist(theaterId):
    return get_movies_by_theatre(theaterId)

# This method will get all the seats for the selecetd movies and selacted theater, input is theater id and movie id
@app.route('/showSeats/<theaterId>/<movieId>', methods=['GET'])
def  showSeatsForMovie(theaterId,movieId):
    return showSeats(theaterId,movieId)

# This method will cancel the booking for the user, input is booking id
@app.route('/cancelTickets/<bookingId>', methods=['GET'])
def  cancelBooking(bookingId):
    return cancelUserBooking(bookingId)

# This method will update the booking name for the user, input is booking id and new customer name
@app.route('/updateTickets/<bookingId>/<newCustomerName>', methods=['GET'])
def  updateBooking(bookingId,newCustomerName):
    return updateCustomerName(bookingId,newCustomerName)

# This method will  book the tickets for the user, input is customerName, customerAge, theaterId, movieId selectedSeats
@app.route('/bookTickets/<customerName>/<customerAge>/<theaterId>/<movieId>/<selectedSeats>', methods=['GET'])
def  confirmBooking(customerName,customerAge,theaterId,movieId,selectedSeats):
    return bookTickets(customerName,customerAge,theaterId,movieId,selectedSeats)


# This method will get the tickets for the user, input is booking id
@app.route('/getTicket/<bookingId>', methods=['GET'])
def  getMovieTickets(bookingId):
    return createTicket(bookingId)


if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080')
from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
from booktickets import getBookingsForCustomer as getBookingsForCustomerFromBooking, cancelUserBooking,updateCustomerName,showSeats
# from movieshows import  getTheaters
from movietheaters import getAreas
# from movietheaters import getSeatsForMovie
from movietheaters import get_nearby_theaters
from movieshows import get_movies_by_theatre

mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'web'
app.config['MYSQL_PASSWORD'] = 'webPass'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = 'localhost' #for now
mysql.init_app(app)




@app.route('/getBookingsForCustomer/<name>', methods=['GET'])
def  getBookingsForCustomer(name):
    return getBookingsForCustomerFromBooking(name)

@app.route('/getAreaList/', methods=['GET'])
def  getAreaList():
    return getAreas()
    

@app.route('/getTheratersList/<area>', methods=['GET'])
def  getListTheraters(area):
    return get_nearby_theaters(area)

@app.route('/getMovieList/<theaterId>', methods=['GET'])
def  getMovieist(theaterId):
    return get_movies_by_theatre(theaterId)

@app.route('/showSeats/<theaterId>/<movieId>', methods=['GET'])
def  showSeatsForMovie(theaterId,movieId):
    return showSeats(theaterId,movieId)


@app.route('/cancelTickets/<bookingId>', methods=['GET'])
def  cancelBooking(bookingId):
    return cancelUserBooking(bookingId)

@app.route('/updateTickets/<bookingId>/<newCustomerName>', methods=['GET'])
def  updateBooking(bookingId,newCustomerName):
    return updateCustomerName(bookingId,newCustomerName)


if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080')
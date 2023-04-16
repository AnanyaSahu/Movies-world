from flask import Flask
# from flask_mysqldb import MySQL
# from flask_cors import CORS
from flask import Flask, render_template, request
from booktickets import bookTicketsForCustomer
from movietheaters import movieTheater
from movieshows import  getMovieShow
from getTickets import createTicketsForBookings

# mysql = MySQL()
app = Flask(__name__)
# CORS(app)
# mysql.init_app(app)



# This method will get booking deatails for a customer, input is customer name
@app.route('/getBookingsForCustomer/<name>', methods=['GET'])
def  getBookingsForCustomer(name):
    b = bookTicketsForCustomer()
    return b.getBookingsForCustomer(name)

# This method will list all the area
@app.route('/getAreaList/', methods=['GET'])
def  getAreaList():
    mt = movieTheater()
    return mt.getAreas()
    
# This method will list all the theaters ans return a list of theaters ordered by the nearest to farthest area, input is areacode 
@app.route('/getTheratersList/<area>', methods=['GET'])
def  getListTheraters(area):
    mt = movieTheater()
    return mt.get_nearby_theaters(area)

# This method will list all the movies for the selacted theater, input is theater id
@app.route('/getMovieList/<theaterId>', methods=['GET'])
def  getMovieist(theaterId):
    m = getMovieShow()
    return m.get_movies_by_theatre(theaterId)

# This method will get all the seats for the selecetd movies and selacted theater, input is theater id and movie id
@app.route('/showSeats/<theaterId>/<movieId>', methods=['GET'])
def  showSeatsForMovie(theaterId,movieId):
    b = bookTicketsForCustomer()    
    return b.showSeats(theaterId,movieId)

# This method will cancel the booking for the user, input is booking id
@app.route('/cancelTickets/<bookingId>', methods=['DELETE'])
def  cancelBooking(bookingId):
    b = bookTicketsForCustomer()
    return b.cancelUserBooking(bookingId)

# This method will update the booking name for the user, input is booking id and new customer name
@app.route('/updateTickets/<bookingId>/<newCustomerName>', methods=['POST'])
def  updateBooking(bookingId,newCustomerName):
    b = bookTicketsForCustomer()
    return b.updateCustomerName(bookingId,newCustomerName)

# This method will  book the tickets for the user, input is customerName, customerAge, theaterId, movieId selectedSeats
@app.route('/bookTickets/<customerName>/<customerAge>/<theaterId>/<movieId>/<selectedSeats>', methods=['POST'])
def  confirmBooking(customerName,customerAge,theaterId,movieId,selectedSeats):
    b = bookTicketsForCustomer()    
    return b.bookTickets(customerName,customerAge,theaterId,movieId,selectedSeats)


# This method will get the tickets for the user, input is booking id
@app.route('/getTicket/<bookingId>', methods=['GET'])
def  getMovieTickets(bookingId):
    c= createTicketsForBookings()
    return c.createTicket(bookingId)

# This will render the template on cloud
@app.route('/')
def  landPage():
    return render_template('template/index.html')

if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080', ssl_context=('../cert.pem', '../privkey.pem'))


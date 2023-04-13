from database import openDbConnection
from flask import Flask
app = Flask(__name__)

seatDictionary = {}
# fetches selected seats from database and add marker to if the seat is booked or available
def showSeats(theaterId,movieId):
    listOfSeatBooked =[]
    cursor = openDbConnection()
    getTherterQuery = "SELECT [thearerName],[areaId],[rowRange],[ColumnRange] FROM [movieDb].[dbo].[Theater] where [theaterId] = "+theaterId +";"
    getBookedTickets = "SELECT [seatBooked] FROM [movieDb].[dbo].[Booking] where [theraterId] = "+theaterId +" AND [movieId]='"+ movieId  +"';"
    cursor.execute(getTherterQuery)
    record = cursor.fetchall()
    row = record[0][2].split(',')
    column =  record[0][3].split(',')
    listOfSeats = []
    seatDictionary = {} 
    cursor.execute(getBookedTickets)
    record = cursor.fetchall()
    for i in record:
        i[0].split(',')
        listOfSeatBooked += i[0].split(',')
    for i in range (ord(row[1])-ord(row[0])+1):
        for j in range(int(column[0]), int(column[1])+1):
             seat = chr(ord('A') + i) + '-' + str(j)
             listOfSeats.append(seat)
             if(seat in listOfSeatBooked): seatDictionary[seat] = 'B'
             else: seatDictionary[seat] = 'A'
    
    outputDict = {'row': row, 'column': column ,'seats': seatDictionary}
    return {'rows':outputDict}

# Book tickets for customer with customer name ,theater, movie name, selected seate, and age
def bookTickets(customerName, customerAge ,theraterId, movieId,seats):
    cursor = openDbConnection()
    movieQuery = "SELECT [movieId],[movieName],[ageConstraint] FROM [movieDb].[dbo].[Movie] WHERE [movieId]= "+movieId+";"
    getBookingQuery = "SELECT * FROM [movieDb].[dbo].[Booking] WHERE theraterId = " + theraterId+" AND movieId = "+movieId+" AND customerName = '" + customerName+"' AND seatBooked = '"+ seats+"';"
    record = cursor.execute(movieQuery).fetchall()
    if(int(customerAge) >= record[0][2]):
        bookTicketsQuery = "INSERT INTO [movieDb].[dbo].[Booking] ([theraterId],[movieId],[seatBooked],[customerName]) VALUES(?,?,?,?);"
        cursor.execute(bookTicketsQuery, theraterId , movieId, seats,customerName)
        cursor.commit()
        record = cursor.execute(getBookingQuery).fetchall()
        r= [tuple(row) for row in record]
        return {'rows': r}
    # if age of customer is less than age constraint of movie tickets will not be booked 
    else: return {'rows':[],'msg':'Your booking is unsuccessful due to age constraint'}


#delete the booking for the user
def cancelUserBooking( bookingId):
    cursor = openDbConnection()
    cancelBookingQuery = "DELETE FROM [movieDb].[dbo].[Booking] WHERE [bookingId]= "+bookingId
    cursor.execute(cancelBookingQuery)
    cursor.commit()
    return {'msg':'Your booking has been cancelled'}

# get booking details for a user with user name
def  getBookingsForCustomer(name):
    cursor = openDbConnection()
    getBookingsForCustomerQuery = "SELECT b.bookingId , b.customerName, b.seatBooked ,m.movieId,m.movieName , m.showTiming, t.theaterId, t.thearerName from [movieDb].[dbo].[Booking] b Inner join [movieDb].[dbo].[Theater] t on t.theaterId = b.theraterId Inner join [movieDb].[dbo].[Movie] m on m.movieId = b.movieId where b.customerName ='"+name +"';" 
    record = cursor.execute(getBookingsForCustomerQuery).fetchall()
    r= [tuple(row) for row in record]
    return {'rows': r}

#update customer name for and existing booking
def updateCustomerName(bookingID, newCustomerName):
    cursor = openDbConnection()
    updateCustomerNameQuery = "UPDATE [movieDb].[dbo].[Booking] SET [customerName] = '"+ newCustomerName+"' WHERE [bookingID]= "+bookingID
    cursor.execute(updateCustomerNameQuery)
    cursor.commit()
    return {'msg':'Your booking has been modified'}
from database import openDbConnection
from flask import Flask
from flask import request
import json
app = Flask(__name__)
# 
# INSERT INTO [dbo].[Area] ([areaName],[location]) VALUES('Parnell Street' ,'100')
# INSERT INTO [dbo].[Movie] ([movieName] ,[showTiming] ,[duration] ,[ageConstraint]) VALUES ('Ant-Man and The Wasp: Quantumania','1330','110 min','14');
# INSERT INTO [dbo].[Theater]([thearerName],[areaId],[rowRange],[ColumnRange]) VALUES('Cine World','A,B','1,5');
# INSERT INTO [dbo].[Booking]([theraterId]  ,[movieId] ,[seatBooked]  ,[customerName]) VALUES  (104,107,'B-2,B-3','Baran')
seatDictionary = {}

def showSeats(theaterId,movieId):
    listOfSeatBooked =[]
    cursor = openDbConnection()
    getTherterQuery = "SELECT [thearerName],[areaId],[rowRange],[ColumnRange] FROM [movieDb].[dbo].[Theater] where [theaterId] = "+theaterId +";"
    getBookedTickets = "SELECT [seatBooked] FROM [movieDb].[dbo].[Booking] where [theraterId] = "+theaterId +" AND [movieId]='"+ movieId  +"';"
    cursor.execute(getTherterQuery)
    print( 'record')
    record = cursor.fetchall()
    print( record)
    row = record[0][2].split(',')
    column =  record[0][3].split(',')
    # print( column)
    # print( record[0][3].split(','))
    listOfSeats = []
    seatDictionary = {} 
    cursor.execute(getBookedTickets)
    record = cursor.fetchall()
    for i in record:
        i[0].split(',')
        listOfSeatBooked += i[0].split(',')
    # print(listOfSeatBooked)
    for i in range (ord(row[1])-ord(row[0])+1):
        for j in range(int(column[0]), int(column[1])+1):
             seat = chr(ord('A') + i) + '-' + str(j)
             listOfSeats.append(seat)
             if(seat in listOfSeatBooked): seatDictionary[seat] = 'B'
             else: seatDictionary[seat] = 'A'
    
    outputDict = {'row': row, 'column': column ,'seats': seatDictionary}
    print(outputDict)
    return {'rows':outputDict}
     
    
# return seats booked n available in theater


# def selectSeats( theraterId, movieId,seatRow, ColumnStart, numberOfSeats):
#     # if endof column in row is less tha startcolumn + number of seats donot allow selection
#     cursor = openDbConnection()
#     getTherterQuery = "SELECT [rowRange],[ColumnRange] FROM [movieDb].[dbo].[Theater] where [theaterId] = "+theraterId +";"
#     record = cursor.execute(getTherterQuery)
#     if(ColumnStart+numberOfSeats >  record[0][2]):
#         pass  
    

# retrun the seat in format row-column


def bookTickets(customerName, customerAge ,theraterId, movieId,seats  ):
    # if endof column in row is less tha startcolumn + number of seats donot allow selection
    cursor = openDbConnection()
    movieQuery = "SELECT [movieId],[movieName],[ageConstraint] FROM [movieDb].[dbo].[Movie] WHERE [movieId]= "+movieId+";"
    getBookingQuery = "SELECT * FROM [movieDb].[dbo].[Booking] WHERE theraterId = " + theraterId+" AND movieId = "+movieId+" AND customerName = '" + customerName+"' AND seatBooked = '"+ seats+"';"
    record = cursor.execute(movieQuery).fetchall()
    if(int(customerAge) >= record[0][2]):
        bookTicketsQuery = "INSERT INTO [movieDb].[dbo].[Booking] ([theraterId],[movieId],[seatBooked],[customerName]) VALUES(?,?,?,?);"
        print(bookTicketsQuery)
        cursor.execute(bookTicketsQuery, theraterId , movieId, seats,customerName)
        cursor.commit()
        record = cursor.execute(getBookingQuery).fetchall()
        r= [tuple(row) for row in record]
        return {'rows': r}
    else: return {'rows':[],'msg':'Your booking is unsuccessful due to age constraint'}
        
    
    
# RETURN BOOKED TICKET with customer name tehater name movie name seats



def cancelUserBooking( bookingId):
    #delete the booking
    cursor = openDbConnection()
    cancelBookingQuery = "DELETE FROM [movieDb].[dbo].[Booking] WHERE [bookingId]= "+bookingId
    print(cancelBookingQuery)
    cursor.execute(cancelBookingQuery)
    cursor.commit()
    return {'msg':'Your booking has been cancelled'}

def  getBookingsForCustomer(name):
    cursor = openDbConnection()
    getBookingsForCustomerQuery = "SELECT b.bookingId , b.customerName, b.seatBooked ,m.movieId,m.movieName , m.showTiming, t.theaterId, t.thearerName from [movieDb].[dbo].[Booking] b Inner join [movieDb].[dbo].[Theater] t on t.theaterId = b.theraterId Inner join [movieDb].[dbo].[Movie] m on m.movieId = b.movieId where b.customerName ='"+name +"';" 
    print(getBookingsForCustomerQuery)
    record = cursor.execute(getBookingsForCustomerQuery).fetchall()
    r= [tuple(row) for row in record]
    return {'rows': r}


def updateCustomerName(bookingID, newCustomerName):
    #delete the booking
    cursor = openDbConnection()
    updateCustomerNameQuery = "UPDATE [movieDb].[dbo].[Booking] SET [customerName] = '"+ newCustomerName+"' WHERE [bookingID]= "+bookingID
    print(updateCustomerNameQuery)
    cursor.execute(updateCustomerNameQuery)
    cursor.commit()
    return {'msg':'Your booking has been modified'}


# bookTickets(104,107,'B-1','Divya',19)
# cancelBooking('104','107',"'B-1'","'Divya'")
# showSeats('104','107')
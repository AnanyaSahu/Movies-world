from database import databaseConnection

class bookTicketsForCustomer:
    def __init__(self):
        pass
        
    seatDictionary = {}
    # fetches selected seats from database and add marker to if the seat is booked or available
    def showSeats(self,theaterId,movieId):
        listOfSeatBooked =[]
        d = databaseConnection()
        cursor = d.openDbConnection()
        getTherterQuery = "SELECT [thearerName],[areaId],[rowRange],[ColumnRange] FROM [MoviesWorld].[dbo].[Theater] where [theaterId] = "+theaterId +";"
        getBookedTickets = "SELECT [seatBooked] FROM [MoviesWorld].[dbo].[Booking] where [theraterId] = "+theaterId +" AND [movieId]='"+ movieId  +"';"
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
    def bookTickets(self,customerName, customerAge ,theraterId, movieId,seats):
        d = databaseConnection()
        cursor = d.openDbConnection()
        movieQuery = "SELECT [movieId],[movieName],[ageConstraint] FROM [MoviesWorld].[dbo].[Movie] WHERE [movieId]= "+movieId+";"
        getBookingQuery = "SELECT * FROM [MoviesWorld].[dbo].[Booking] WHERE theraterId = " + theraterId+" AND movieId = "+movieId+" AND customerName = '" + customerName+"' AND seatBooked = '"+ seats+"';"
        record = cursor.execute(movieQuery).fetchall()
        if(int(customerAge) >= record[0][2]):
            bookTicketsQuery = "INSERT INTO [MoviesWorld].[dbo].[Booking] ([theraterId],[movieId],[seatBooked],[customerName]) VALUES(?,?,?,?);"
            cursor.execute(bookTicketsQuery, theraterId , movieId, seats,customerName)
            cursor.commit()
            record = cursor.execute(getBookingQuery).fetchall()
            r= [tuple(row) for row in record]
            return {'rows': r}
        # if age of customer is less than age constraint of movie tickets will not be booked 
        else: return {'rows':[],'msg':'Your booking is unsuccessful due to age constraint'}


    #delete the booking for the user
    def cancelUserBooking( self,bookingId):
        d = databaseConnection()
        cursor = d.openDbConnection()
        cancelBookingQuery = "DELETE FROM [MoviesWorld].[dbo].[Booking] WHERE [bookingId]= "+str(bookingId)
        cursor.execute(cancelBookingQuery)
        cursor.commit()
        return {'msg':'Your booking has been cancelled'}

    # get booking details for a user with user name
    def  getBookingsForCustomer(self,name):
        d = databaseConnection()
        cursor = d.openDbConnection()
        getBookingsForCustomerQuery = "SELECT b.bookingId , b.customerName, b.seatBooked ,m.movieId,m.movieName , m.showTiming, t.theaterId, t.thearerName from [MoviesWorld].[dbo].[Booking] b Inner join [MoviesWorld].[dbo].[Theater] t on t.theaterId = b.theraterId Inner join [MoviesWorld].[dbo].[Movie] m on m.movieId = b.movieId where b.customerName ='"+name +"';" 
        record = cursor.execute(getBookingsForCustomerQuery).fetchall()
        r= [tuple(row) for row in record]
        return {'rows': r}

    #update customer name for and existing booking
    def updateCustomerName(self,bookingID, newCustomerName):
        d = databaseConnection()
        cursor = d.openDbConnection()
        updateCustomerNameQuery = "UPDATE [MoviesWorld].[dbo].[Booking] SET [customerName] = '"+ newCustomerName+"' WHERE [bookingID]= "+str(bookingID)

        cursor.execute(updateCustomerNameQuery)
        cursor.commit()
        return {'msg':'Your booking has been modified'}
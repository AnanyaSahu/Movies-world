from database import openDbConnection
# 
# INSERT INTO [dbo].[Area] ([areaName],[location]) VALUES('Parnell Street' ,'100')
# INSERT INTO [dbo].[Movie] ([movieName] ,[showTiming] ,[duration] ,[ageConstraint]) VALUES ('Ant-Man and The Wasp: Quantumania','1330','110 min','14');
# INSERT INTO [dbo].[Theater]([thearerName],[areaId],[rowRange],[ColumnRange]) VALUES('Cine World','A,B','1,5');
# INSERT INTO [dbo].[Booking]([theraterId]  ,[movieId] ,[seatBooked]  ,[customerName]) VALUES  (104,107,'B-2,B-3','Baran')

def showSeats(theaterId,movieId):
    listOfSeatBooked =[]
    cursor = openDbConnection()
    getTherterQuery = "SELECT [thearerName],[areaId],[rowRange],[ColumnRange] FROM [movieDb].[dbo].[Theater] where [theaterId] = "+theaterId +";"
    getBookedTickets = "SELECT [seatBooked] FROM [movieDb].[dbo].[Booking] where [theraterId] = "+theaterId +" AND [movieId]='"+ movieId  +"';"
    cursor.execute(getTherterQuery)
    record = cursor.fetchall()
    print( record)
    # print( record[0][2])
    column =  record[0][3].split(',')
    # print( record[0][3].split(','))
    listOfSeats = []
    seatDictionary = {} 
    cursor.execute(getBookedTickets)
    record = cursor.fetchall()
    for i in record:
        i[0].split(',')
        listOfSeatBooked += i[0].split(',')
    # print(listOfSeatBooked)
    for i in range (0,ord('B')-ord('A')+1):
        for j in range(int(column[0]), int(column[1])+1):
             seat =chr(ord('A') + i) + '-' + str(j)
             listOfSeats.append(seat)
             if(seat in listOfSeatBooked): seatDictionary[seat] = 'B'
             else: seatDictionary[seat] = 'A'
    
    print(seatDictionary)
    return seatDictionary
     
    
# return seats booked n available in theater


def selectSeats( theraterId, movieId,seatRow, ColumnStart, numberOfSeats):
    # if endof column in row is less tha startcolumn + number of seats donot allow selection
    cursor = openDbConnection()
    getTherterQuery = "SELECT [rowRange],[ColumnRange] FROM [movieDb].[dbo].[Theater] where [theaterId] = "+theraterId +";"
    record = cursor.execute(getTherterQuery)
    if(ColumnStart+numberOfSeats >  record[0][2]):
        pass  
    

# retrun the seat in format row-column


def bookTickets(theraterId, movieId,seats, customerName, customerAge ):
    # if endof column in row is less tha startcolumn + number of seats donot allow selection
    cursor = openDbConnection()
    # bookTicketsQuery = "INSERT INTO [dbo].[Booking] ([theraterId],[movieId],[seatBooked],[customerName]) VALUES("+theraterId +","+ movieId+",'"+seats+"','"+customerName+"');"
    bookTicketsQuery = "INSERT INTO [dbo].[Booking] ([theraterId],[movieId],[seatBooked],[customerName]) VALUES(?,?,?,?);"
    print(bookTicketsQuery)
   
    cursor.execute(bookTicketsQuery, theraterId , movieId, seats,customerName)
    # record = cursor.fetchall()
    # print(record)

    pass
# RETURN BOOKED TICKET with customer name tehater name movie name seats

def calculateRemaingSeats(bookedSeats,theraterId, movieId ):
    # if endof column in row is less tha startcolumn + number of seats donot allow selection
    pass


# showSeats('104','107')
bookTickets(102,107,'B-1','Divya',19)
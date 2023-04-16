import unittest
from unittest.mock import MagicMock, Mock

from booktickets import bookTicketsForCustomer
from getTickets import createTicketsForBookings
from movietheaters import movieTheater
from movieshows import getMovieShow
from database import databaseConnection


def t():unittest.main(argv=['ignore'],exit=False)

class TestStringMethods(unittest.TestCase):

    def test_updateCustomerName(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       b = bookTicketsForCustomer()
       result = b.updateCustomerName(123,'ananya')
       self.assertEqual(result['msg'], 'Your booking has been modified')

    def test_getBookingsForCustomer(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       b = bookTicketsForCustomer()
       result = b.getBookingsForCustomer('ananya')
       self.assertGreaterEqual(len(result['rows']), 0)

    def test_cancelUserBooking(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       b = bookTicketsForCustomer()
       result = b.cancelUserBooking(123)
       self.assertEqual(result['msg'], 'Your booking has been cancelled')

    def test_getAreas(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       s = movieTheater()
       result = s.getAreas()
       self.assertGreaterEqual(len(result['rows']), 0)


    def test_get_nearby_theaters(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       s = movieTheater()
       result = s.get_nearby_theaters(100)
       self.assertGreaterEqual(len(result['rows']), 0)


    def test_createTicket(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       s = createTicketsForBookings()
       result = s.createTicket(100)
       self.assertGreaterEqual(len(result['rows']), 0)
        
    def test_get_movies_by_theatre_with_valid_theatre_id(self):
       cursor= Mock()
       db = databaseConnection()
       db.openDbConnection = MagicMock(return_value=cursor)
       s = getMovieShow()
       result = s.get_movies_by_theatre(101)
       self.assertGreaterEqual(len(result['rows']), 0)
    
    def test_get_movies_for_invalid_theatre_id(self):
       # Test with an invalid theatre ID
       s = getMovieShow()
       result = s.get_movies_by_theatre(99)
       self.assertGreaterEqual(len(result['rows']), 0)

if __name__ == '__main__':
    unittest.main()

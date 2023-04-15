import unittest
from unittest.mock import MagicMock, Mock

from booktickets import bookTicketsForCustomer
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


if __name__ == '__main__':
    unittest.main()
import config
from datetime import datetime
import MySQLdb
import re
import traceback


_connected = False
_database = None
_cursor = None

# setupConnection() must be called before anything else for this to work
# closeConnection() should be called after finishing


def setupConnection():
    global _connected
    global _database
    global _cursor

    if not _connected:
        try:
            _database = MySQLdb.connect(host="localhost",
                                        user="root",
                                        passwd=config.password,
                                        db="gttravel")
            _cursor = _database.cursor()
            _connected = True
        except Exception as e:
            _connected = False
            traceback.print_exc()


def closeConnection():
    global _connected

    if _connected:
        _database.close()
        _connected = False








# testing
setupConnection()

# print writeReview()
# code for SELECT for testing :)
# _cursor.execute("SELECT * FROM city_language")
# for row in _cursor.fetchall():
#     print row
# print citySearch(None, None, None, None, None)

closeConnection()

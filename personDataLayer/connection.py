from logger_base import log
import psycopg2 as bd
import sys


class Connection:
    _DATABASE = 'test_db_udemy'
    _USERNAME = 'linuxdev'
    _PASSWORD = '123'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _connection = None
    _cursor = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = bd.connect(host=cls._HOST,
                                             user=cls._USERNAME,
                                             password=cls._PASSWORD,
                                             port=cls._DB_PORT,
                                             database=cls._DATABASE
                                             )
                log.debug(f'Connection successful :{cls._connection}')
                return cls._connection
            except Exception as e:
                log.error(f'There was an exception to get the connection {e}')
                sys.exit()  # this is to ensure everything is close, finish the software
        else:
            return cls._connection

    @classmethod
    def get_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f'the cursor has opened correctly : {cls._cursor} ')
                return cls._cursor
            except Exception as e:
                log.error(f'There was an exception to get the cursor : {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Connection.get_connection()
    Connection.get_cursor()
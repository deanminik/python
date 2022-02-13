from logger_base import log
from psycopg2 import pool
import sys


class Connection:
    _DATABASE = 'test_db_udemy'
    _USERNAME = 'linuxdev'
    _PASSWORD = '123'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Creation of pool successful : {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'There was an error to get the pool : {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def get_connection(cls):
        pass


if __name__ == '__main__':
    pass

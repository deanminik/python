import sys
from psycopg2 import pool
from logger_base import log


class Connection:
    # private variables class (_)
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
                log.debug(f'Creation of the pool in the project user lab was successful :{cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'There was an error to start with the pool')
                sys.exit()
        else:
            return cls._pool

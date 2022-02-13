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

    @classmethod
    def get_connection(cls):
        # here we call the object from the pool
        connection = cls.get_pool().getconn()
        log.debug(f'Connection got it from the pool : {connection}')
        return connection

    @classmethod
    def release_connection(cls, connection):
        cls.get_pool().putconn(connection) # put back to the pool
        log.debug(f'We put back the object connection to the pool : {connection}')

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall() # all connection from the pool will close
        log.debug('all connection from the pool were closed')


if __name__ == '__main__':
    connection1 = Connection.get_connection()
    Connection.release_connection(connection1)
    Connection.close_connection()
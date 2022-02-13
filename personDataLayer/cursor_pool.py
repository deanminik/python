from logger_base import log
from personDataLayer.connection import Connection


class CursorOfPool:
    def __init__(self):
        self._connection = None
        self._cursor = None

    # Implementing the resource manager
    # this will be activated when we invoke (with)
    def __enter__(self):
        log.debug('Start the method (with __enter__)')
        self._connection = Connection.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    # end (with)
    def __exit__(self, exc_type, exc_value, exc_detail):
        # correct ->
        # incorrect -> roll back
        log.debug('Execute the method exit')
        if exc_value: # if different to None
            self._connection.rollback()
            log.error(f'There was an error, rollback: {exc_value} {exc_type} {exc_detail}')
        else:
            self._connection.commit()
            log.debug('Commit of the transaction')

        self._cursor.close()
        Connection.release_connection(self._connection)



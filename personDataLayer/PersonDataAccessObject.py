from personDataLayer.connection import Connection
from personDataLayer.cursor_pool import CursorOfPool
from personDataLayer.person import Person
from logger_base import log


class PersonDAO:
    # class variable
    _SELECT = 'SELECT * FROM person ORDER BY id_person'
    _INSERT = 'INSERT INTO person(per_name, per_lastname, per_email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE person SET per_name=%s, per_lastname=%s, per_email=%s WHERE id_person=%s'
    _DELETE = 'DELETE FROM person WHERE id_person=%s'

    @classmethod
    def select(cls):

        with CursorOfPool() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            persons = []
            for register in registers:
                person = Person(register[0], register[1], register[2], register[3])
                persons.append(person)
            return persons

    @classmethod
    def insert(cls, person):
        with CursorOfPool() as cursor: # CursorOfPool() from enter and exit we have created in cursor_pool
            values = (person.name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)
            # check this commit https://github.com/deanminik/python/commit/633113556ad2fc596fb31192f7bdbffc0df9abd3
            log.debug(f'Person to insert : {person}')
            return cursor.rowcount

    @classmethod
    def update(cls, person):
        with CursorOfPool() as cursor:
            values = (person.name, person.last_name, person.email, person.id_person)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Person Updated :{person}')
            return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with CursorOfPool() as cursor:
            values = (person.id_person,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Person Deleted :{person}')
            return cursor.rowcount


if __name__ == '__main__':
    # ->Insert an object
    # person1 = Person(name='patito 3', last_name='new last name 3', email='new email 3')
    # persons_inserted = PersonDAO.insert(person1)
    # log.debug(f'Persons inserted : {persons_inserted}')

    # -> Update an object
    person1 = Person(7, 'lukas', 'Update-lastname 6', 'Update-email 6')
    persons_updated = PersonDAO.update(person1)
    log.debug(f'Persons Updated: {persons_updated}')

    # -> Delete an object
    # person1 = Person(id_person=7)
    # persons_deleted = PersonDAO.delete(person1)
    # log.debug(f'Persons Deleted: {persons_deleted}')

    # -> selection of objects
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)


'''
output
02:10:14 AM: DEBUG [cursor_pool.py:13] Start the method (with __enter__)
02:10:14 AM: DEBUG [connection.py:27] Creation of pool successful : <psycopg2.pool.SimpleConnectionPool object at 0x7f6599030be0>
02:10:14 AM: DEBUG [connection.py:38] Connection got it from the pool: <connection object at 0x7f659902b180; dsn: 'user=linuxdev password=xxx dbname=test_db_udemy host=localhost port=5432', closed: 0>
02:10:14 AM: DEBUG [cursor_pool.py:22] Execute the method exit
02:10:14 AM: DEBUG [cursor_pool.py:28] Commit of the transaction
02:10:14 AM: DEBUG [connection.py:45] We put back the connection to the pool: <connection object at 0x7f659902b180; dsn: 'user=linuxdev password=xxx dbname=test_db_udemy host=localhost port=5432', closed: 0>
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 1, Name: Update-name
                Last name: Update-lastname, Email: Update-email
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 2, Name: updated name
                Last name: updated last name, Email: updated email
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 6, Name: updated name
                Last name: updated last name, Email: updated email
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 8, Name: Mari
                Last name: Barker, Email: mymail@gmail.com
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 9, Name: Mari
                Last name: Barker, Email: mymail@gmail.com
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 10, Name: Mari
                Last name: Barker, Email: mymail@gmail.com
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 11, Name: Mari
                Last name: Barker, Email: mymail@gmail.com
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 25, Name: New user
                Last name: new last name, Email: new email
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 26, Name: New user 2
                Last name: new last name 2, Email: new email 2
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 27, Name: New user 2
                Last name: new last name 2, Email: new email 2
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 28, Name: New user 2
                Last name: new last name 2, Email: new email 2
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 29, Name: New user 2
                Last name: new last name 2, Email: new email 2
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 30, Name: New user
                Last name: new last name, Email: new email
               
02:10:14 AM: DEBUG [PersonDataAccessObject.py:71] 
                Id Person: 31, Name: New user 3
                Last name: new last name 3, Email: new email 3
'''
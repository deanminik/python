from personDataLayer.connection import Connection
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
        with Connection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registers = cursor.fetchall()
                persons = []
                for register in registers:
                    person = Person(register[0], register[1], register[2], register[3])
                    persons.append(person)
                return persons

    @classmethod
    def insert(cls, person):
        with Connection.get_connection() as connection:
            with connection.cursor() as cursor:
                values = (person.name, person.last_name, person.email)
                cursor.execute(cls._INSERT, values)
                # check this commit https://github.com/deanminik/python/commit/633113556ad2fc596fb31192f7bdbffc0df9abd3
                log.debug(f'Person to insert : {person}')
                return cursor.rowcount

    @classmethod
    def update(cls, person):
        with Connection.get_connection() as connection:
            with Connection.get_cursor() as cursor:
                values = (person.name, person.last_name, person.email, person.id_person)
                cursor.execute(cls._UPDATE, values)
                log.debug(f'Person Updated :{person}')
                return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with Connection.get_connection() as connection:
            with Connection.get_cursor() as cursor:
                values = (person.id_person,)
                cursor.execute(cls._DELETE, values)
                log.debug(f'Person Deleted :{person}')
                return cursor.rowcount


if __name__ == '__main__':
    # ->Insert an object
    # person1 = Person(name='New user 3', last_name='new last name 3', email='new email 3')
    # persons_inserted = PersonDAO.insert(person1)
    # log.debug(f'Persons inserted : {persons_inserted}')

    # -> Update an object
    # person1 = Person(7, 'Update-name 6', 'Update-lastname 6', 'Update-email 6')
    # persons_updated = PersonDAO.update(person1)
    # log.debug(f'Persons Updated: {persons_updated}')

    # -> Delete an object
    person1 = Person(id_person=7)
    persons_deleted = PersonDAO.delete(person1)
    log.debug(f'Persons Deleted: {persons_deleted}')

    # -> selection of objects
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)

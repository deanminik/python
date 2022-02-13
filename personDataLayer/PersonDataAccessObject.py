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
        with Connection.get_cursor() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            persons = []
            for register in registers:
                person = Person(register[0], register[1], register[2], register[3])
                persons.append(person)
            return persons


if __name__ == '__main__':
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)

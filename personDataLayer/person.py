from logger_base import log


class Person:
    def __init__(self, id_person=None, name=None, last_name=None, email=None):
        # with None we can avoid adding the parameter when we are going to create an object
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return f'''
                Id Person: {self._id_person}, Name: {self._name}
                Last name: {self._last_name}, Email: {self._email}
               '''

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        self._id_person = id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    pers1 = Person(15, 'pepe', 'hdz', 'mi@hotmail.com')
    log.debug(pers1)
    # Simulate an Insert
    pers1 = Person(name='pepe', last_name='hdz', email='mi@hotmail.com')
    log.debug(pers1)
    # simulate a Delete
    pers1 = Person(id_person=1)
    log.debug(pers1)

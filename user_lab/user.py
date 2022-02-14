from logger_base import log


class User:
    # with None we can avoid adding the parameter when we are going to create an object
    def __init__(self, id_user=None, username=None, password=None):
        self._id_user = id_user
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
                    Id User: {self._id_user}, 
                    Username: {self._username}, 
                    Password: {self._password}
                '''

    # getter and setter
    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':
    user1 = User(15, 'shaimeco', '123')
    log.debug(user1)
    # Simulate an Insert
    user1 = User(username='pepe', password='777')
    log.debug(user1)
    # simulate a Delete
    user = User(id_user=1)
    log.debug(user1)

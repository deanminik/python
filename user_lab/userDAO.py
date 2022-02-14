from user_lab.cursor_pool import CursorOfPool
from user_lab.user import User
from logger_base import log


class UserDAO:
    _SELECT = 'SELECT * FROM public."User" ORDER BY id_user'
    _INSERT = 'INSERT INTO public."User"(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE public."User" SET username=%s, password=%s WHERE id_user=%s'
    _DELETE = 'DELETE FROM public."User" WHERE id_user=%s'

    @classmethod
    def select(cls):
        with CursorOfPool() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            users = []
            for register in registers:
                user = User(register[0], register[1], register[2])
                users.append(user)
            return users


    @classmethod
    def insert(cls, user):
        with CursorOfPool() as cursor:  # CursorOfPool() from enter and exit we have created in cursor_pool
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)
            # check this commit https://github.com/deanminik/python/commit/633113556ad2fc596fb31192f7bdbffc0df9abd3
            log.debug(f'Person to insert : {user}')
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with CursorOfPool() as cursor:
            values = (user.username, user.password, user.id_user)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Person Updated :{user}')
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with CursorOfPool() as cursor:
            values = (user.id_user,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Person Deleted :{user}')
            return cursor.rowcount


if __name__ == '__main__':
    # ->Insert an object
    # user1 = User(username='patito 3', password='3')
    # user_inserted = UserDAO.insert(user1)
    # log.debug(f'Users inserted : {user_inserted}')

    # -> Update an object
    # user1 = User(2,password='44455555')
    # user_updated = UserDAO.update(user1)
    # log.debug(f'Users Updated: {user_updated}')

    # -> Delete an object
    # user1 = User(id_user=5)
    # users_deleted = UserDAO.delete(user1)
    # log.debug(f'User Deleted: {users_deleted}')

    # -> selection of objects
    users = UserDAO.select()
    for user in users:
        log.debug(user)
        # log.debug(user.id_user, user.username, user.password)

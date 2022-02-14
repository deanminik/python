from user_lab.user import User
from user_lab.userDAO import UserDAO
from logger_base import log

option = None
while option != 5:
    print('Options')
    print('1 - Linting users')
    print('2 - Add users')
    print('3 - Update user')
    print('4 - Delete user')
    print('Exit')
    option = int(input('Type the option :'))
    if option == 1:
        users = UserDAO.select()
        for user in users:
            log.info(user)
    if option == 2:
        username_var = input('add username')
        password_var = input('add password')
        user = User(username=username_var, password=password_var)
        users_inserted = UserDAO.insert(user)
        log.info(f'Users inserted: {users_inserted}')
    if option == 3:
        id_user_var = int(input('Add the id to change the value'))
        username_var = input('add the new username')
        password_var = input('add the new password')
        user = User(id_user_var,username_var,password_var)
        users_updated = UserDAO.update(user)
        log.info(f'User updated : {users_updated}')
    if option == 4:
        id_user_var = int(input('Add the id to delete'))
        user = User(id_user=id_user_var)
        user_deleted = UserDAO.delete(user)
        log.info(f'Users deleted : {user_deleted}')
else:
    print('Out of application')


import psycopg2

connection = psycopg2.connect(
    user='linuxdev',
    password='123',
    host='localhost',
    port='5432',
    database='test_db_udemy'
)
try:
    with connection:
        with connection.cursor() as cursor:
            sentence = 'SELECT id_person, per_name FROM person WHERE id_person IN %s'
            # primary_keys = ((1,2,3),) # tuple of tuples
            entry = input('Add the ids separated with commas like this |1,2,3...| :')
            # now convert into tuple  split to delete the (',') to return only the numbers
            primary_keys = (tuple(entry.split(',')),) # tuple of tuples -> ((1,2,3),)
            cursor.execute(sentence, primary_keys)
            registers = cursor.fetchall()
            for register in registers:
                print(register)
except Exception as e:
        print(f'There was an error :{e}')
finally:
    # success or not do this
    connection.close()

'''
(1, 'Pedro')
(2, 'Marco')
'''
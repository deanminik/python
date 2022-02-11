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
            sentence = 'DELETE FROM person WHERE id_person IN %s'
            entry = input('Add the id or ids you want to delete example-> 1, 2, .. :')
            values = (tuple(entry.split(',')),)
            cursor.execute(sentence, values)
            registers_deleted = cursor.rowcount
            print(f'Register deleted :{registers_deleted}')

except Exception as e:
        print(f'There was an error :{e}')
finally:
    connection.close()

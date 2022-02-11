import psycopg2

connection = psycopg2.connect(
    user='linuxdev',
    password='123',
    host='localhost',
    port='5432',
    database='test_db_udemy'
)
try:
    with connection: # we have to close manually instead we have with
        with connection.cursor() as cursor: # close automatically
            sentence = 'SELECT * FROM person'
            cursor.execute(sentence)
            registers = cursor.fetchall()
            print(registers)
except Exception as e:
        print(f'There was an error :{e}')
finally:
    # success or not do this
    connection.close()

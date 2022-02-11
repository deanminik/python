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
            sentence = 'UPDATE person SET per_name=%s, per_lastname=%s, per_email=%s WHERE id_person=%s'
            values = ('updated name','updated last name','updated email',2)
            cursor.execute(sentence, values)
            # connection.commit() # to save the data in our db but (with) has that method
            registers_updated = cursor.rowcount
            print(f'Register inserted :{registers_updated}')

except Exception as e:
        print(f'There was an error :{e}')
finally:
    connection.close()

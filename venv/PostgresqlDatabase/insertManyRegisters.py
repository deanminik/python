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
            sentence = 'INSERT INTO person(per_name, per_lastname, per_email) VALUES(%s, %s, %s)'
            values =(
                        ('Rita2','Hdz2','ulacit2@hotmail.com'),
                        ('Rita3','Hdz3','ulacit3@hotmail.com'),
                        ('Rita4','Hdz4','ulacit4@hotmail.com')
            ) #tuple of tuples
            cursor.executemany(sentence, values)
            # connection.commit() # to save the data in our db but (with) has that method
            registers_inserted = cursor.rowcount
            print(f'Register inserted :{registers_inserted}')

except Exception as e:
        print(f'There was an error :{e}')
finally:
    connection.close()

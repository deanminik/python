import psycopg2 as bd

connection = bd.connect(
    user='linuxdev',
    password='123',
    host='localhost',
    port='5432',
    database='test_db_udemy'
)
try:
   with connection:
       with connection.cursor() as cursor:
           sentence = 'INSERT INTO person(per_name, per_lastname, per_email) VALUES (%s, %s, %s)'
           values = ('Mari++++', 'Barker', 'mymail@gmail.com')
           cursor.execute(sentence, values)

           sentence = 'UPDATE person SET per_name=%s, per_lastname=%s, per_email%s WHERE id_person=%s'
           values = ('Juank','rodriguez','hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',1)
           cursor.execute(sentence, values)

except Exception as e:
        print(f'There was an error, so we made a roll back  :{e}')
finally:
    connection.close()

print('transaction finished)')
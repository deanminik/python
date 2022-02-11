import psycopg2 as bd

connection = bd.connect(
    user='linuxdev',
    password='123',
    host='localhost',
    port='5432',
    database='test_db_udemy'
)
try:
   connection.autocommit = False # this is to don't save the changes automatically
   cursor = connection.cursor()
   sentence = 'INSERT INTO person(per_name, per_lastname, per_email) VALUES (%s, %s, %s)'
   values = ('Mari', 'Barker', 'mymail@gmail.com')
   cursor.execute(sentence, values)
   connection.commit() # to save the changes manually
   print('transaction done')
except Exception as e:
        connection.rollback() # if something happens then go back and stored the registers
        print(f'There was an error, so we made a roll back  :{e}')
finally:
    connection.close()

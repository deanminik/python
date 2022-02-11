import psycopg2

connection = psycopg2.connect(
    user='linuxdev',
    password='123',
    host='localhost',
    port='5432',
    database='test_db_udemy'
)

print(connection) # just to see if the connection is successful
'''
<connection object at 0x7f4edbd53040; dsn: 'user=linuxdev password=xxx dbname=test_db_udemy host=localhost port=5432', closed: 0>
'''

cursor = connection.cursor() # this allows to execute sql sentence in postgresql
sentence = 'SELECT * FROM person'
cursor.execute(sentence)
# so that was just to get the data
# Now we need to keep the data like an object in a variable
registers = cursor.fetchall()
print(registers)
'''
[(1, 'Pedro', 'Fdz', 'email1-@gmail.com'), (2, 'Marco', 'Torres', 'email2-@gmail.com'), (3, 'Luis', 'Monge', 'email3-@gmail.com')]
'''

# so we have a list with tuples

# Now it is important to close the connection (our cursor)
cursor.close()
connection.close()

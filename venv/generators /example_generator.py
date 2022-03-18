# number generator from 1 to 5
def number_generator():
    for number in range(1,6):
        yield number
        print('start with the execution')



# We use our object generator
generator = number_generator()
print(f' Object generator : {generator}')
"""
 Object generator : <generator object number_generator at 0x7f39999ca120>
"""

# consume the generator with next or for
for value in generator:
    print(f'number generated: {value}')

"""
number generated: 1
start with the execution
number generated: 2
start with the execution
number generated: 3
start with the execution
number generated: 4
start with the execution
number generated: 5
start with the execution
"""
print('consume by demand'.center(50,'*'))
# consume by demand
generator_v2 = number_generator()
print(f'Consuming by demand: {next(generator_v2)}')
print(f'Consuming by demand: {next(generator_v2)}')

"""
Consuming by demand: 1
start with the execution
Consuming by demand: 2
"""

print('consume by demand with try and catch '.center(50,'*'))
# consume by demand
generator_v3 = number_generator()
try:

    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')
    print(f'Consuming by demand: {next(generator_v2)}')

except StopIteration as e:
    print(f'You are demanding more than 5 numbers available {e}')
"""
You are demanding more than 5 numbers available 
"""

print('consume by demand with (while)'.center(50,'*'))
generator_while = number_generator()

while True:
    try:
        value = next(generator_while)
        print(f'Print of the value generated: {value}')
    except StopIteration as e:
        print('The iterator has finished ')
        break # stop the while 


"""
**********consume by demand with (while)**********
Print of the value generated: 1
start with the execution
Print of the value generated: 2
start with the execution
Print of the value generated: 3
start with the execution
Print of the value generated: 4
start with the execution
Print of the value generated: 5
start with the execution
The iterator has finished 
"""
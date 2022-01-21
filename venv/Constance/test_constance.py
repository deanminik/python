#from constance import * # (*) the meaning  is to import the all modules
from constance import MY_CONSTANCE
from constance import Mathematics as Math # (math is an alias )


print(MY_CONSTANCE)
MY_CONSTANCE = 'New value'
print(MY_CONSTANCE)
#print(Mathematics.PI)
print(Math.PI)

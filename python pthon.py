import random
from random import randint

user = int(input("Quantas jogadas e necessarias para os dados darem numeros iguas? "))
jogadas = 0
dado_1 = 1
dado_2 = 2
while dado_1 != dado_2:
    jogadas += 1
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)

if jogadas == user:
    print ("acertou!")
else:
    print (f'Foram necessarias {jogadas}, por isso tente novmente!')

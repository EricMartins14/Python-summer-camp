import random
numero = int(input("escolhe um numero"))
numero_aleatorio = random.randint(1, 5)
if numero == numero_aleatorio:
    print ("tu estas correto")
else:
    print ("tu nao estas correto")
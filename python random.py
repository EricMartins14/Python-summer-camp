import random
numero = int(input("escolhe um numero"))
numero_aleatorio = random.randint(1, 100)

while numero != numero_aleatorio:
    if numero < numero_aleatorio:
        print ("mais alto")
        numero = int(input("escolhe um numero outra vez"))
    elif numero > numero_aleatorio:
        print ("mais baixo")
        numero = int(input("escolhe um numero outra vez"))

print ("CONSEGUISTE!")



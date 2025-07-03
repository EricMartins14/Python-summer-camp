from time import sleep

n1 = int(input("Escohe o primeiro numero"))
n2 = int(input("Escohe o segundo numero"))

if n1 % 2 != 0:
    n1 += 1

for x in range (n1, n2, 2 ):
    print (x)
    


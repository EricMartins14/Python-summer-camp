from time import sleep

frase = input("Insira aqui a frase: ")
letra = input("Insira aqui a letra que esta a procura: ")

contador = 0
for x in frase:
    if x == letra:
        contador += 1

if contador == 0:
    print("Nao foi econtrado  letra que escolhei")
else:
    print(f'A letra "{letra}" foi econtrado {contador} numero de vezes')
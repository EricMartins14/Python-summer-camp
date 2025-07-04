pergunta1 = input(" o que e melhor youtube ou youtube kids")
pergunta2 = input(" o que e melhor sushi ou burger king")
pergunta3 = input(" o que e melhor bicicleta ou  slider scooter v2")
pergunta4 = input(" o que e melhor fortnite  ou  minecraft")
pergunta5 = input(" o que e melhor limonada  ou  limonada de frutos vermelhos")

correta = ["youtube","sushi","slider scooter v2","minecraft","limonada de frutos vermelhos"]
contador = 0
for x in pergunta1,pergunta3, pergunta4, pergunta5:
    if x == correta:
        contador += 1

if contador != 0:
    print(f'A resposta "{correta}" foi econtrado {contador} numero de vezes')
else:
    print("Nao acertaste nenhuma resposta")
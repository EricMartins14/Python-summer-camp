nota1 = int(input("qual foi a nota do test 1"))
nota2 = int(input("qual foi a nota do test 2"))
media = (nota1 * nota2) / 2
if media < 60:
    print ("voce nao pasou")
else:
    print("voce pasou")
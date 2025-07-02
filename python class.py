from datetime import date

data_nascimento = int(input("quale tua data nascimento"))
idade = data_nascimento - date.today().year
if idade < 18:
    print ("es demasido novo")
elif idade < 55:
    print ("podes ir")
else:
    print ("es demasiado velho")
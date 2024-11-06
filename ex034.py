salario = float(input('qual o seu salario ?: R$ '))
if salario > 1250:
    salario = salario + (salario * 10/100)
else:
    salario = salario + (salario * 15/100)
print('Seu novo salario é R$ {:.2f}'.format(salario))
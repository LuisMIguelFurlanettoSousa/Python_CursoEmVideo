num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um numero [para parar o programa só digitar 999]: '))
    soma = soma + num
    cont = cont + 1
print('A soma dos numeros é {}'.format(soma - 999))
print(('Voçe digitou {} numeros'.format(cont - 1)))

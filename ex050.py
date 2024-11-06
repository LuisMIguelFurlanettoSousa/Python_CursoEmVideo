'''soma = 0
for c in range(1, 7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma entre os numeros PARES que voçe colocou é {}'.format(soma))'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voçê informou {} numeros PARES e a soma foi {}'.format(cont, soma))

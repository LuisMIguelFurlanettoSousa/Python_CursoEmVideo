'''print('-=' * 20)
print('SOMA ENTRE OS NUMEROS MULTIPLOS DE 3 (IMPARES) DE 1 A 500')
print('-=' * 20)
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos {} valores solicitados é {}'.format(c, soma))'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitaods é {}'.format(cont, soma))
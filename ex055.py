maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa ?: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O MAIOR peso é {}Kg'.format(maior))
print('O MENOR peso é {}Kg'.format(menor))

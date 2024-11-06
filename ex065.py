continuar = ''
cont = 0
soma = 0
maior = 0
menor = 0

while continuar != 'NAO':

    num = int(input('Digite um numero: '))
    continuar = str(input('Deseja continuar [SIM/NAO]: ')).strip().upper()

    cont = cont + 1
    soma = soma + num

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

media = soma / cont

print('A media entre os numero é {:.2f}'.format(media))
print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))

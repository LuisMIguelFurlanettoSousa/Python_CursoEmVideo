numbers = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))

print(f'Você digitou {numbers}')

print(f'O numero 9 apareceu {numbers.count(9)} vezes')

if 3 in numbers:
    print(f'O numero 3 esta na {numbers.index(3) + 1}ª posiçao')
else:
    print('O numero 3 nao foi digitado em nenhuma posiçao')

print('Os valores pares digitados foram: ', end='-')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')

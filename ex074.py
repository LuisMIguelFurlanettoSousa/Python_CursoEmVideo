from random import randint


numbers = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

print('os valores sorteados foram:', end=' ')
for n in numbers:
    print(f' {n}', end=' ')

print(f'\nO numero maior é {max(numbers)}')
print(f'O numero menor é {min(numbers)}')

lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um numero para a posiçao {c}: ')))


print('-=' * 20)
print(f'A lista foi : {lista}')
print(f'O maior numero da lista é {max(lista)}, nas posiçoes', end=' ')
for p, v in enumerate(lista):
    if v == max(lista):
        print(f'{p}...', end='')
print()
print(f'O menor numero da lista é {min(lista)}, nas posiçoes', end=' ')
for p, v in enumerate(lista):
    if v == min(lista):
        print(f'{p}...', end='')
print()

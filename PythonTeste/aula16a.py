lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('-=' * 20)
for comida in lanche:
    print(comida)
print('-=' * 20)
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}, posiçao {cont}')
print('-=' * 20)
for pos, comida in enumerate(lanche):
    print(f'{comida}, posiçao {pos}')

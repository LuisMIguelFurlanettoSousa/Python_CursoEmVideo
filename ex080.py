lista = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posiçao {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
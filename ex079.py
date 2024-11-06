lista = []
while True:
    num = int(input('Digite um numero: '))
    if num in lista:
        print('VALOR DUPLICADO, nao vou adicionar...')
    else:
        print('Valor adicionado...')
        lista.append(num)
    resp = str(input('Deseja continuar [S/N]?: ')).upper().strip()[0]
    if resp in 'N':
        break

print('-=' * 30)
print(f'A sua lista em ordem crescente é {sorted(lista)}')

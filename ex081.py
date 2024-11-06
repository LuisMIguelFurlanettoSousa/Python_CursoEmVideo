lista = []
while True:

    num = int(input('Digite um numero: '))
    lista.append(num)

    resp = str(input('Deseja continuar [S/N] ?: ')).strip().upper()[0]
    while resp not in 'SN':
        print('Resposta invalida')
        resp = str(input('Deseja continuar [S/N] ?: ')).strip().upper()[0]
    if resp == 'N':
        break

print(lista)
print('-=' * 30)
print(f'Você digitou {len(lista)} numeros')

lista.sort(reverse=True)
print(f'Lista em ordem decrescente {lista}')

if 5 in lista:
    print('O numero 5 apareceu na lista')
else:
    print('O numero 5 nao apareceu na lista')

lista = []
lista_impar = []
lista_par = []

while True:
    num = int(input('Digite um numero: '))
    lista.append(num)

    if num == 0:
        lista_impar.append(num)
        lista_par.append(num)
    if num % 2 == 0 and num != 0:
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)

    resp = str(input('Deseja continuar [S/N] ?:')).strip().upper()[0]
    while resp not in 'SN':
        print('resposta invalida, ', end='')
        resp = str(input('Deseja continuar [S/N] ?:')).strip().upper()[0]
    if resp in 'N':
        break
print(lista)
print(f'Os numeros pares da lista sao : {lista_par}')
print(f'Os numeros impares da lista sao: {lista_impar}')

from random import randint
from time import sleep

def sorteia(list):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(n, end=' ' ,flush=True)
        sleep(0.3)
    print('PRONTO!')


def SomaPar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = [] 
sorteia(numeros)
SomaPar(numeros)

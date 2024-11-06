from random import randint
from time import sleep
azul = '\033[36m'
vermelho = '\033[31m'
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada ?: '))
if jogador not in [0, 1, 2]:
    print('RESPOSTA INVALIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
    print('-=' * 11)
    print('Computador jogou {}{}\033[m'.format(vermelho, itens[computador]))
    print('O jogador jogou {}{}\033[m'.format(azul, itens[jogador]))
    print('-=' * 11)

    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCEU')
        elif jogador == 2:
            print('COMPUTADOR VENCEU')
    if computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCEU')
    if computador == 2:
        if jogador == 0:
            print('JOGADOR VENCEU')
        elif jogador == 1:
            print('COMPUTADOR VENCEU')
        elif jogador == 2:
            print('EMPATE')

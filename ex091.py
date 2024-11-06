from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()

print('VALORES SORTEADOS')
for j in range(1, 5):
    jogadores[f'Jogador {j}'] = randint(1, 6)

ranking = list()
for k, v in jogadores.items():
        print('{:>22}'.format(f'O {k} tirou {v}'))
        sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('  ==RANKING DOS JOGADORES==  ')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
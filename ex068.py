from random import randint
from time import sleep

vitoria = 0

while True:
    print('=-' * 20)
    print('JOGO DE IMPAR OU PAR')
    print('=-' * 20)

    impar_par = str(input('Voçê quer IMPAR (I) PAR (P): ')).strip().upper()[0]
    while impar_par not in 'IP':
        impar_par = str(input('Voçê quer IMPAR (I) PAR (P): ')).strip().upper()[0]

    jogador = int(input('Informe um numero : '))

    computador = randint(0, 10)
    soma = jogador + computador

    if impar_par == 'P':
        print('PAR!!!')
        sleep(1)
        print('IMPAR!!')
        sleep(2)
        print(f'voçê jogou {jogador}, e eu joguei {computador} o total deu {soma}')
        if soma % 2 == 0:
            print('Voçe venceu')
            vitoria += 1
        elif jogador == 0 and computador == 0:
            print('EMPATAMOS, ambos escolhemos 0, então irei considerar essa rodada')
        else:
            print('VOÇÊ PERDEU')
            break

    elif impar_par == 'I':
        print('IMPAR!!')
        sleep(1)
        print('PAR!!')
        sleep(2)
        print(f'voçê jogou {jogador}, e eu joguei {computador} o total deu {soma}')
        if soma % 2 == 0:
            print('VOÇÊ PERDEU')
            break
        elif jogador == 0 and computador == 0:
            print('EMPATAMOS, ambos escolhemos 0, então irei considerar essa rodada')
        else:
            print('Voçê venceu')
            vitoria += 1

if vitoria > 3:
    print(f'INCRIVEL!!, voçê conseguiu me vencer {vitoria} vezes CONSECUTIVAS')
else:
    print(f'PARABENS, voçê me venceu {vitoria} vezes')

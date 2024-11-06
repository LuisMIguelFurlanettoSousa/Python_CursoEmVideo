from random import randint

num_aleatorio = randint(0, 10)
palpites = 0
acertou = False

while not acertou:
    chute = int(input('tente acertar um numero de 0 à 10: '))
    palpites += 1
    if chute == num_aleatorio:
        print('VOÇÊ ACERTOU, com {} tentativas'.format(palpites))
        acertou = True
    else:
        if chute > num_aleatorio:
            print('Menos... Tente novamente')
        elif chute < num_aleatorio:
            print('Mais... Tente novamente')

print('FIM DE JOGO')

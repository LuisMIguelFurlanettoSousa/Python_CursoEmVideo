from random import randint
from time import sleep
num_aleatorio = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 ate 5, tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que numero pensei ?: '))
print('PROCESSANDO...')
sleep(2)
if num == num_aleatorio:
    print('Parabens voce acertou o numero')
else:
    print('infelismente voce errou eu pensei no numero {} não no {}'.format(num_aleatorio, num))

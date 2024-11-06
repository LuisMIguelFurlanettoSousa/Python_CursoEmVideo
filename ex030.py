num = int(input('qual o numero ?: '))
par_impar = num % 2
if par_impar == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))

from math import factorial
num = 0
resultado = 0
while num != -1:
    num = int(input('informe o numero : '))
    resultado = factorial(num)
    print('{}! = {}'.format(num, resultado))


num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
if num1 > num2:
    print('O primeiro valor, {}, é o maior'.format(num1))
elif num2 > num1:
    print('O segundo valor, {}, é o maior'.format(num2))
elif num1 == num2:
    print('Sao enguais')

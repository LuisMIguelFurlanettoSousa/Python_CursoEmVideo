from time import sleep
r1 = float(input('informe a primeira reta: '))
r2 = float(input('informe a segunda reta: '))
r3 = float(input('informe a terceira reta: '))
print('-=' * 20)
print('ANALIZANDO...')
print('-=' * 20)
sleep(3)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('PODE formar um triangulo!')
else:
    print('NÃO PODE formar um triangulo!')
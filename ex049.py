'''tabuada = int(input('Voçê quer a tabuada de qual numero ?: '))
multiplicacao = 0
for c in range(0, 11):
    print('{} x {} = {}'.format(tabuada, multiplicacao, tabuada * multiplicacao))
    multiplicacao = multiplicacao + 1'''
num = int(input('Digite um numero : '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

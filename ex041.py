from datetime import date
azul = '\033[36m'
vermelho = '\033[31m'
nascimento = int(input('Em que ano voce nasceu ?: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Voçê é um nadador {}MIRIM'.format(azul))
elif idade > 9 and idade <= 14:
    print('Voçê é um nadador {}INFANTIL'.format(azul))
elif idade > 14 and idade <= 19:
    print('Voçê é um nadador {}JUNIOR'.format(azul))
elif idade > 19 and idade <= 25:
    print('Voçê é um nadador {}SENIOR',format(azul))
else:
    print('NADADOR {}MASTERRRRRRRRRRR!!!!!!'.format(vermelho))
from datetime import date
print('-=' * 20)
print('1 - Masculino\n2 - Feminino')
print('-=' * 20)
sexo = int(input('Qual o seu genero, [1 ou 2] ?: '))
if sexo == 1:
    nasc = int(input('Qual ano que voce nasceu?: '))
    idade = date.today().year - nasc
    if idade < 18:
        print('Voçê ainda irá se alistar, ainda falta {} anos'.format(18 - idade))
        print('Seu alistamento vai ser em {}'.format(nasc + 18))
    elif idade == 18:
        print('Esta na hora de voçê se alistar')
    else:
        print('Ja passou {} anos de seu alistamento'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(nasc + 18))
if sexo == 2:
    print('Voçê NÃO precisa se alistar no exercito')

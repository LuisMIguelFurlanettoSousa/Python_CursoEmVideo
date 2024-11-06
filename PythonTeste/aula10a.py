'''nome = str(input('Qual o seu nome ?: '))
if nome == 'Julia':
    print('que nome divino, eu amo tanto a Julia Ferreira Caitano!!')
else:
    print('que nome xoxo')
print('bom dia, {}!'.format(nome))'''
n1 = float(input('qual a sua primiera nota ?: '))
n2 = float(input('qual a sua segunda nota ?: '))
n3 = float(input('qual a sua terceira nota ?: '))
m = (n1 + n2 + n3) / 3
print('sua media foi de {:.2f}'. format(m))
if m >= 6:
    print('Parabens sua media esta boa!!')
else:
    print('sua media nao esta boa!!, ESTUDE MAISS')

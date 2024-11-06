azul = '\033[36m'
vermelho = '\033[31m'
amarelo = '\033[33m'
roxo = '\033[35m'
print('-=' * 20)
print('CALCULADORA IMC')
print('-=' * 20)
peso = float(input('Primeiro informe seu peso (kg): '))
altura = float(input('Informme a sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} \n{}ABAIXO DO PESO'.format(imc, vermelho))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} \n{}PESO IDEAl'.format(imc, azul))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} \n{}SOBREPESO'.format(imc, amarelo))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} \n{}OBESIDADE'.format(imc, vermelho))
else:
    print('Seu IMC é {:.2f} \n{}OBESIDADE MÓRBIDA'.format(imc, roxo))

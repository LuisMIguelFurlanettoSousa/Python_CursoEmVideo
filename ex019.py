from random import choice
nome1 = str(input('qual o primeiro nome ?: '))
nome2 = str(input('qual o segundo nome ?: '))
nome3 = str(input('qual o terceiro nome ?: '))
nome4 = str(input('qual o quarto nome ?:'))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('o nome escolhido foi: {}'.format(escolhido))
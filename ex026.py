frase = str(input('Digite uma frase: ')).strip().upper()
print('Sua frase tem {} A '.format(frase.count('A')))
print('O primeiro A aparece na posiçao {}'.format(frase.find('A') + 1))
print('O ultimo A aparece na posiçao {}'.format(frase.rfind('A') + 1))

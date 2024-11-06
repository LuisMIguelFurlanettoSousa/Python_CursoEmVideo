from datetime import date
ano_atual = date.today().year
somaM = 0
somam = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu ?: '.format(c)))
    idade = ano_atual - ano
    if idade >= 21:
        somaM = somaM + 1
    elif idade < 21:
        somam = somam + 1
print('Ao todo tem {} pessoas MAIORES de idade'.format(somaM))
print('Ao toma tem {} pessoas MENORES de idade'.format(somam))

primeiro_termo = int(input('Qual o primeiro termo da PA ?: '))
razao = int(input('Qual a razão da PA ?: '))

termo = primeiro_termo
cont = 0
termos_extras = 10
total = 0

while termos_extras != 0:
    total = total + termos_extras
    while cont <= total:
        print(termo, end=' ')
        termo = termo + razao
        cont = cont + 1

    termos_extras = int(input('\nMais quantos termos (se digitar 0 o programa encerra)?: '))
print('progreçao finalizada com {} termos'.format(total))

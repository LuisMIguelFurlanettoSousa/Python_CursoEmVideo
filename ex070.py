tot_gasto = 0
valor_mil = 0
cont = 0
valor_mais_barato = 0
while True:
    print('-=' * 20)
    print('{:^40}'.format('COMPRAS'))
    print('-=' * 20)
    nome_produto = str(input('Nome produto: ')).strip()
    valor = float(input('Valor: R$'))

    cont += 1
    tot_gasto += valor

    if valor > 1000:
        valor_mil += 1

    if cont == 1 or valor < valor_mais_barato:
        valor_mais_barato = valor
        produto_mais_barato = nome_produto

    continuar = ' '

    while continuar not in 'SN':
        print('-' * 40)
        continuar = str(input('Deseja adicionar mais produtos [S/N] ?: ')).strip().upper()[0]

    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total gasto foi de \033[31mR${tot_gasto:.2f}\033[m')
print(f'\033[31m{valor_mil}\033[m produtos custam mais de R$1000,00')
print(f'O produto mais barato é \033[31m{produto_mais_barato}\033[m com o valor de \033[31mR${valor_mais_barato:.2f}\033[m')

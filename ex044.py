preco = float(input('informe o preço total dos produtos: '))
print('-=' * 20)
print('1 - PAGAMENTO EM DINHEIRO / CHEQUE: 10% de desconto '
      '\n2 - À VISTA NO CARTÃO: 5% de desconto'
      '\n3 - Em até 2X NO CARTÃO: Preço normal'
      '\n4 - Em 3X OU MAIS: 20% de juros')
print('-=' * 20)
pagamento = int(input('Qual das opçoes acima voçê irá querer: '))
if pagamento == 1:
    preco = preco - (preco * 10/100)
elif pagamento == 2:
    preco = preco - (preco * 5/100)
elif pagamento == 3:
    preco = preco
    parcelas = preco / 2
    print('Sua compra sera pacelada em 2x de R${:.2f}'.format(parcelas))
elif pagamento == 4:
    preco = preco + (preco * 20/100)
    parcelas = int(input('Em quantas vezes voçe quer parcelar ?'))
    total = preco / parcelas
    print('Sua compra vai ser dividida em {}x e o valor de cada parcela sera de R${:.2f}'.format(parcelas, total))
else:
    preco = 0
    print('Opçao invalida')
print('Com o metodo de pagamento escolhido o valor ficou R${:.2f}'.format(preco))

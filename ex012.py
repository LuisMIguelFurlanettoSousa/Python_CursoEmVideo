preco = float(input('qual o valor do produto ?: R$'))
novo = preco - (preco * (5/100))
print('o produto que antes custava R${} agora com 5% de desconto custara RS{}'.format(preco, novo))

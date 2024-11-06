real = float(input('quantos reais voçê tem ?: R$'))
dollar = real / 5.51
euro = real / 5.89
iene = real / 0.034
print('voçe pode comprar com R${} US$ {:.2f} '.format(real, dollar))
print('voçe pode comprar com R${} € {:.2f}'.format(real, euro))
print('voçe pode comprar com R${} ¥ {:.2f}'.format(real, iene))
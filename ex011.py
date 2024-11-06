largura = float(input('qual é a largura da parede ?:'))
altura = float(input('qual é a altura da parede ?:'))
area = largura * altura
print('A sua parede tem a dimensão de {}x{} e tem a area de {:.2f} M²'.format(largura, altura, area))
tinta = area / 2
print('voçe precisara de {:.2f}L de tinta'.format(tinta))
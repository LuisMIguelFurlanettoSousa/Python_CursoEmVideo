from definiçoes import moeda

p = float(input('informe o preço: R$ '))
print(f'A metade do {moeda.formatado(p)} é {moeda.formatado(moeda.metade(p))}')
print(f'O dobro de {moeda.formatado(p)} é {moeda.formatado(moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.formatado(moeda.aumentar(p, 10))}')
print(f'Diminuindo 15% temos {moeda.formatado(moeda.diminuir(p, 15))}')
from definiçoes import moeda

p = float(input('informe o preço: R$ '))
print(f'A metade do {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 15% temos {moeda.diminuir(p, 15)}')
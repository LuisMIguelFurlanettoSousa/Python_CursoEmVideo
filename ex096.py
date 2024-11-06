def area(l, c):
    area = l * c
    print(f'A area de um terreno {l}x{c} é de {area}m²')


print('{:-^30}'.format('controle de terreno'))

Largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(Largura, comprimento)
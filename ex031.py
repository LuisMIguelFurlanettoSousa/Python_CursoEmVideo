viagem = float(input('quantos quilometros deu a sua viagem ?: '))
if viagem > 200:
    valor = viagem * 0.45
    print('o valor da viagem ficou em R$ {:.2f} pois foi uma viagem de mais de 200 km '.format(valor))
else:
    valor = viagem * 0.5
    print('o valor da viagem ficou em R$ {:.2f}'.format(valor))

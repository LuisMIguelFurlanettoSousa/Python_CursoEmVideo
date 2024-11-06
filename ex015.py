dia = int(input('Quantos dias o carro ficou alugado ?: '))
km = float(input('Quantos quilometros foram rodados ?: '))
pago = (dia * 60) + (km * 0.15)
print('voce utilizou o carro por {} dias e {} km isso ira dar o valor de R${:.2f}'.format(dia, km, pago))
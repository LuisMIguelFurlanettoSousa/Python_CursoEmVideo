velo = int(input('qual a velocidade que voce passou ?: '))
if velo > 80:
    multa = (velo - 80) * 7
    print('voçê foi MULTADO!, excedeu o limite permitido de 80Km/h, terá que pagar R${:.2f}'.format(multa))
else:
    print('Tudo certo!, boa viagem')

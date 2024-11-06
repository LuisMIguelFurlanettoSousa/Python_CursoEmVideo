print('=-' * 20)
print('{:^40}'.format('CAIXA ELETRONICO'))
print('=-' * 20)

saque = int(input('Qual o valor que voçê deseja sacar ?: '))
total = saque
ced = 50
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'total de {tot_ced} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break


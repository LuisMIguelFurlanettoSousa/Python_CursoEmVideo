nota1 = float(input('qual sua primeira nota ?: '))
nota2 = float(input('qual a sua segunda nota ?: '))
m = (nota1 + nota2) / 2
if m < 5:
    print('Sua media foi {:.2f}, Reprovado'.format(m))
elif m >= 5 and m < 7:
    print('Sua media foi {:.2f}, Recuperação'.format(m))
else:
    print('Sua media foi {:.2f}, APROVADO'.format(m))
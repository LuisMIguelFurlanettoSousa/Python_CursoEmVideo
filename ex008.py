m = float(input('quantos metros ?:'))
cm = m * 100
mm = m * 1000
km = m / 1000
print('{} metros é equivalente a {:.2f} centimetros e {:.2f} milimetros'.format(m, cm, mm))
print('A quantidade em kilometros é {} km'.format(km))
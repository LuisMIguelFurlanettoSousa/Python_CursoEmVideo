from math import hypot
co = float(input('qual o valor do cateto oposto ?: '))
ca = float(input('qual o valo do cateto adjacente ?: '))
hi = hypot(co, ca)
print('A hipotenuza é {:.2f}'.format(hi))
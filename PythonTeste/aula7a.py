n1 = int(input('digite um numero :'))
n2 = int(input('digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print('A sona é {} \na multiplicaçao é {} \na divisao é {}, ' .format(s, m, d),end='')
print('a divisao inteiro é {} \na ponteciaçao é {} \no resto da divisão é {}' .format(di, e, rd))
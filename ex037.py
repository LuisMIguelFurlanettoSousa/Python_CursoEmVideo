num = int(input('Digite um numero inteiro: '))
print('-=' * 20)
print('1 - Binario\n2 - octal\n3 - hexadecial')
print('-=' * 20)
base = int(input('Sua opção [1, 2 ou 3]: '))
if base == 1:
    print('O numero {} em base binaria e´{}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O numero {} em base octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O numero {} em base hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')

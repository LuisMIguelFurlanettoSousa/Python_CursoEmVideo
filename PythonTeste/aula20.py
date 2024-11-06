'''def titulo(txt):
    print('-='  * 30)
    print(txt)
    print('-='  * 30)

titulo('guanabara ')'''

'''def soma(a, b):
    print(f'a = {a}, b = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(a=4, b=5)
soma(8, 9)'''

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao {tam} numeros', end='')
    print('')


contador(2, 1, 7)
contador (8, 0)
contador(4, 6, 4, 7, 2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 6, 8, 4, 5, 3]
dobra(valores)
print(valores)
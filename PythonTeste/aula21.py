def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

'''n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {factorial(n)}')'''

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Os resultados sao: {f1}, {f2}, {f3}')
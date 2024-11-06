numero = list()
pares = list()
impares = list()

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}o. numero: '))

    if num % 2 == 0:
        pares.append(num)

    elif num % 2 == 1:
        impares.append(num)
numero.append(pares)
numero.append(impares)

print(numero)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores impares digitados forma: {numero[1]}')
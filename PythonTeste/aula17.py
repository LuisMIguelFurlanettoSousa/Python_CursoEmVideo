'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('nao achei o numero 4')
print(num)
print(f'Esse lista tem {len(num)} elementos') '''

valores = list()

'''valores.append(5)
valores.append(9)
valores.append(4)'''

for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posiçao {c}, tem o numero {v}')
print('Cheguei ao final da lista')


# Criando uma lista
lista1 = [1, 2, 3]

# Igualando lista2 a lista1
lista2 = lista1

# Modificando lista2
lista2.append(4)

# Imprimindo ambas as listas
print("lista1:", lista1)  # Saída: lista1: [1, 2, 3, 4]
print("lista2:", lista2)  # Saída: lista2: [1, 2, 3, 4]

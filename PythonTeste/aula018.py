'''teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Luis'
teste[1] = 17
galera.append(teste[:])
print(teste)
print(f'{galera}')'''

'''galera = [['joao', 15], ['julia', 16], ['luis', 17], ['pedro', 18]]
print(galera[0] [0])'''

galera = list()
dado = list()
maior_idade = menor_idade = 0

for c in range(0, 2):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior_idade += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor_idade += 1 

print(f'temos {maior_idade} pessoas maiores de idade e {menor_idade} pessoas menores de idade')
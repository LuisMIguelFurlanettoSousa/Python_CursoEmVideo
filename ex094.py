lista = list()
dados = dict()
soma_idade = 0

while True:
    dados['Nome'] = str(input('Nome: ')).strip()
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['Sexo'] in 'MF':
            break
        else:
            print('ERRO!! Por favor, digite apenas M ou F.')

    dados['Idade'] = int(input('Idade: '))
    soma_idade += dados['Idade']
    lista.append(dados.copy())
    dados.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Resnposta invalida, tente novamente.')
    if continuar == 'N':
        break

print(f'─ O grupo tem {len(lista)} pessoas')
media = soma_idade / len(lista)
print(f'─ A media de idade é {media:5.2f} anos')
print(f'─ As mulheres cadastradas foram:', end=' ')
for p in lista:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end=' ')
print('\n')
print('Lista das pessoas que estao a cima da media', end='')
for p in lista:
    if p['Idade'] >= media:
        print('  \n   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
'''pessoas = list()
dados = list()
mais_pesado = list()
mais_leve = list()

while True:

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja inserir mais uma pessoa [S/N] ?: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Resopsta invalida tente novamente, deseja inserir mais uma pessoa [S/N] ?: ')).strip().upper()[0]
    if continuar in 'N':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A pessoa mais pesada é {max(pessoas)}')
print(f'A pessoa mais leve é {min(pessoas)}')
'''

temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg, peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

idade_18 = 0
homens = 0
mulheres_menor_20 = 0

while True:
    print('=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('=-' * 20)
    idade = int(input('Qual a sua idade ?: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]

    print('-' * 40)

    if idade >= 18:
        idade_18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_menor_20 += 1

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Voçê informou {idade_18} pessoas com mais de 18 anos')
print(f'Ao todo temos {homens} homens')
print(f'E temos {mulheres_menor_20} mulheres com menos de 20 anos')

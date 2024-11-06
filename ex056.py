soma_idade = 0
maior_idade_homen = 0
nome_mais_velho = ''
totmulher20 = 0

for p in range(1, 5):

    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome ?: ')).strip()
    idade = int(input('Idade ?: '))
    sexo = str(input('Sexo [M / F] ?: ')).strip().upper()
    soma_idade = soma_idade + idade

    '''if p == 1 and sexo == 'M':
        maior_idade_homen = idade
        nome_mais_velho = nome'''# nao achei necessario essa parte do codigo da explicaçao do guanabara

    if sexo == 'M' and idade > maior_idade_homen:
        maior_idade_homen = idade
        nome_mais_velho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 = totmulher20 + 1

media_idade = soma_idade / 4

print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homen mais velho tem {} anos e o seu nome é {}'.format(maior_idade_homen, nome_mais_velho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))


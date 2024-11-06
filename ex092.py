from datetime import date

ano_atual = date.today().year
dados = dict()

dados['Nome'] = str(input('Nome: '))

ano_nascimento =  int(input('ano de nascimento: '))
idade = ano_atual - ano_nascimento
dados['idade'] = idade

dados['Carteira de trabalho'] = int(input('Carteira de trabalho (0 nao tem): '))

if dados['Carteira de trabalho'] != 0:
    dados['Ano de contrataçao'] = str(input('ano de contrataçao: '))
    dados['Salario'] = float(input('salario: '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Ano de contrataçao'] + 35) - ano_atual)

print('=-' * 40)
print(dados)
for k, v in dados.items():
    print(f'  ─ {k} tem o valor de {v}')

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media das notas de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif aluno['Media'] < 7:
    aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'─ {k} é igual a {v}')
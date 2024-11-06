primeiro_termo = int(input('Qual o primeiro termo da PA ?: '))
razao = int(input('Qual a razão da PA ?: '))

termo = primeiro_termo
cont = 1

while cont <= 10:
    print(termo, end=' ')
    termo = termo + razao
    cont = cont + 1

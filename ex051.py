'''primeiro = int(input('Qual vai ser o primeiro termo da PA?: '))
razao = int(input('qual a razão da PA ?: '))
termos = 10 * razao + 1
for c in range(primeiro, termos, razao):
    print(c, end=' ')'''
print('=' * 20)
print('PROGRESÃO ARITIMETICA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo_termo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo_termo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
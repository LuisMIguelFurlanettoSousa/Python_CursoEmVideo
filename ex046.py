'''from time import sleep
print('-=' * 20)
print('FOGOS DE ARTIFICIO')
print('-=' * 20)
lancar = str(input('laçar fogos de artificio [sim ou nao]?: ')).upper().strip()
if lancar == 'SIM':
    print('CONTAGEM REGRESSIVA')
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('Lançamento concluido!!')
else:
    print('laçamento nao autorizado')'''
from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('BUM! BUM! POOOW!')
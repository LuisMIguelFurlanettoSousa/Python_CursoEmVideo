times = ('Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza EC', 'Cruzeiro',
         'São Paulo', 'Bahia', 'Atlético Paranaense', 'Atlético-MG',
         'RB Bragantino', 'Vasco da Gama', 'Criciúma',
         'Juventude', 'Internacional', 'Corinthians', 'Grêmio', 'Vitória',
         'Cuiabá', 'Fluminense', 'Atlético Goianiense')
print('=-' * 20)
print(f'LISTA DE TIMES {times}')
print('=-' * 20)

print(f'os times que estao nas 5 primeiras colocaçoes sao: {times[0:5]}')
'''for c in range(0, 5):
    print(f'{times[c]} na {c + 1}° posiçao')'''
print('=-' * 20)

print(f'os que 4 ultimos colocados sao: {times[-1:-5:-1]}')

'''for c in range(-1, -5, -1):
    print(times[c])'''
print('=-' * 20)

print(f'Os times em ordem alfabetica é: {sorted(times)}')
print('=-' * 20)

print(f'O Flamengo esta na {times.index('Flamengo') + 1}ª posiçao')

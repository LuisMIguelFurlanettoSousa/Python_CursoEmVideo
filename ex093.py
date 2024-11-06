dados = dict()
gols = list()
tot = 0
ip = 1

dados['Nome'] = str(input('Nome: ')).strip()
partidas = int(input(f'Quantas partidas {dados["Nome"]} ja jogou? : '))

for p in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols voçe fez na {p}ª partida?: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('=-' * 30)
print(dados)
print('=-' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('=-' * 30)
print(f'O jogados {dados["Nome"]} jogou {partidas} partidas')

for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols.')

'''for g in dados['gols']:   
    for p in range(ip, partidas + 1):
        print(f'Na partida {p}, fez {g} gols')
        ip += 1
        break'''
dados = dict()
gols = list()
time = list()

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} já jogou? : '))
    gols.clear()

    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols você fez na {p}ª partida?: ')))

    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? : ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Resposta inválida.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i + 1} marcou {g} gols')

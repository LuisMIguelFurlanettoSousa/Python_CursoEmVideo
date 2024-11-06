def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j}, fez {g} gol(s)')


jogador = str(input('Nome: ')).strip()
gols = str(input('Quantos gols ele fez?: ')).strip()

if jogador == '':
    jogador = '<desconhecido>'

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(jogador, gols)
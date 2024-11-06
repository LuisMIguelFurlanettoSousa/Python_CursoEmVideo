from time import sleep

c = {
    "Preto": "\033[30m",
    "Vermelho": "\033[31m",
    "Verde": "\033[32m",
    "Amarelo": "\033[33m",
    "Azul": "\033[34m",
    "Magenta": "\033[35m",
    "Ciano": "\033[36m",
    "Branco": "\033[37m",
    "Cinza": "\033[90m",
    "Vermelho-claro": "\033[91m",
    "Verde-claro": "\033[92m",
    "Amarelo-claro": "\033[93m",
    "Azul-claro": "\033[94m",
    "Magenta-claro": "\033[95m",
    "Ciano-claro": "\033[96m",
    "Branco-claro": "\033[97m",
    "Reset": "\033[0m"
}

def ajuda(h):
    print('~' * 50)
    print('{:^50}'.format(f'ACESSANSO O MANUAL DO COMANDO {h} ...'))
    print('~' * 50)
    sleep(1)

    help(h)

def titulo(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

while True:
    titulo('SISTEMA DE AJUDA PYHELP')

    h = str(input('Funçao ou biblioteca > '))
    if h.upper() == 'FIM':
        titulo('Ate logo!')
        break
    ajuda(h)
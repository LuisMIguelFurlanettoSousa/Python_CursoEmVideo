def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):   
            print('\033[31mErro, digite um numero valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):   
            print('\033[31mErro, digite um numero valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

num = leiaint('digite um inteiro: ')
num1 = leiafloat('digite um numero real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num1}')

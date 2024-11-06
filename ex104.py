def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)) 
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro, digite um numero inteiro valido\033[0m')
        if ok:
            break
    return valor
    

n = leiaint('digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
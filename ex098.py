from time import sleep

def contador(i, f, p):

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print('-=' * 30)
    print(f'Contado de {i} ate {f} de {p} em {p}')

    if i < f:
        c = i
        while c <= f:    
            print(c, end=' ', flush=True)
            c += p
            sleep(0.3)
        print('FIM!!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush=True)
            c -= p
            sleep(0.3)
        print('FIM!')


contador(1, 10, 1)

contador(10, 0 , 2)

print('-=' * 30)
print('Agora é sua vez na contagem!')
i = int(input('INICIO: '))
f = int(input('FIM!: '))
p = int(input('PASSO: '))
contador(i, f, p)

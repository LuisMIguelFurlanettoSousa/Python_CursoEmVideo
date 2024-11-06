while True:
    num = int(input('Voçê quer ver a tabuada de qual valor [Digite um valor negativo para parar] ?: '))
    if num < 0:
        break
    else:
        print('_' * 30)
        for c in range(0, 11):
            print(f'{num} x {c:2} = {num * c}')
        print('_' * 30)

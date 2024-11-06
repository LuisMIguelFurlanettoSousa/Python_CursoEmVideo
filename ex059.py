resposta = -1
resultado = 0

while resposta != 5:

    num1 = float(input('Digite o primiero numero: '))
    num2 = float(input('Digite o segundo numero: '))

    print('''============MENU============
    [1]     SOMAR
    [2]     MULTIPLICAR
    [3]     MAIOR
    [4]     NOVOS NUMEROS
    [5]     SAIR DO PROGRAMA''')

    resposta = int(input('Qual opção voçê deseja ?: '))

    if resposta == 1:
        resultado = num1 + num2
        print('{} + {} = {}'.format(num1, num2, resultado))
    elif resposta == 2:
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))
    elif resposta == 3:
        if num1 > num2:
            print('O maior numero é {}'.format(num1))
        else:
            print('O maior numero é o {}'.format(num2))
    elif resposta == 4:
        print('===== INFORME NOVOS NUMEROS =====')
    elif resposta == 5:
        print('PROGRAMA FINALIZADO')
    else:
        print('\033[31mOPÇÃO INVALIDA, TENTE NOVAMENTE \033[m')

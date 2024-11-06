def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    n (int): O número para o qual se deseja calcular o fatorial. O padrão é 1.
    show (bool): (Opcional) Se True, exibe a multiplicação passo a passo no console.

    Retorno:
    int: O valor do fatorial de 'n'.
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c

    return f

num = int(input('Qual o numero: '))
print(fatorial(num, show=True))
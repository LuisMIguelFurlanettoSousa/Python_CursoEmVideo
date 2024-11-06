def formatado(v = 0, moeda = 'R$'):
    """
    Formata um valor numérico como uma string monetária.

    Parâmetros:
    v (float): O valor numérico a ser formatado.
    moeda (str): O símbolo da moeda a ser usado (padrão é 'R$').

    Retorna:
    str: O valor formatado como string monetária, com duas casas decimais e usando vírgula como separador decimal.
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')


def metade(v, formato = False):
    """
    Calcula a metade de um valor.

    Parâmetros:
    v (float): O valor numérico a ser dividido.
    formato (bool): Se True, formata o resultado como string monetária; se False, retorna o valor bruto (padrão é False).

    Retorna:
    float ou str: A metade do valor, possivelmente formatada como string monetária.
    """
    res = v / 2
    if formato == False:
        return res
    else:
        return formatado(res)


def dobro(v, formato = False):
    """
    Calcula o dobro de um valor.

    Parâmetros:
    v (float): O valor numérico a ser dobrado.
    formato (bool): Se True, formata o resultado como string monetária; se False, retorna o valor bruto (padrão é False).

    Retorna:
    float ou str: O dobro do valor, possivelmente formatado como string monetária.
    """
    res = v * 2
    if formato == False:
        return res
    else:
        return formatado(res)

def aumentar(v, taxa, formato = False):
    """
    Aumenta um valor em uma determinada taxa percentual.

    Parâmetros:
    v (float): O valor numérico base.
    taxa (float): A taxa percentual de aumento.
    formato (bool): Se True, formata o resultado como string monetária; se False, retorna o valor bruto (padrão é False).

    Retorna:
    float ou str: O valor aumentado pela taxa percentual, possivelmente formatado como string monetária.
    """
    res = v + (v * taxa / 100)
    if formato == False:
        return res
    else:
        return formatado(res)

def diminuir(v, taxa, formato = False):
    """
    Diminui um valor em uma determinada taxa percentual.

    Parâmetros:
    v (float): O valor numérico base.
    taxa (float): A taxa percentual de redução.
    formato (bool): Se True, formata o resultado como string monetária; se False, retorna o valor bruto (padrão é False).

    Retorna:
    float ou str: O valor reduzido pela taxa percentual, possivelmente formatado como string monetária.
    """
    res = v - (v * taxa / 100)
    if formato == False:
        return res
    else:
        return formatado(res)
    
def resumo(preco=0, taxaa=10, taxar=5):
    """
    Exibe um resumo das operações financeiras sobre um preço base.

    Parâmetros:
    preco (float): O valor numérico base.
    taxaa (float): A taxa percentual de aumento (padrão é 10%).
    taxar (float): A taxa percentual de redução (padrão é 5%).

    Retorna:
    None: Imprime um resumo formatado das operações financeiras realizadas sobre o valor base.
    """
    print('─' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('─' * 30)
    print(f'Preço analizado: \t{formatado(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('─' * 30)
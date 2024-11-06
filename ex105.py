def notas(*dados, sit=False):

    """
    Calcula várias informações a partir de uma lista de notas e, opcionalmente, avalia a situação do desempenho.

    Parâmetros:
    dados (*float): Um ou mais valores numéricos representando as notas. 
                    Aceita qualquer quantidade de notas, passadas como argumentos variáveis.
    sit (bool): Parâmetro opcional, que indica se a situação do desempenho deve ser incluída no resultado.
                - Se `sit=True`, uma avaliação do desempenho ('Boa', 'Razoavel', 'Ruim') será incluída com base na média das notas.

    Retorno:
    dict: Um dicionário contendo as seguintes informações:
        - 'Qnt_notas': A quantidade de notas fornecidas.
        - 'Maior_nota': A maior nota fornecida.
        - 'Menor_nota': A menor nota fornecida.
        - 'Media': A média das notas fornecidas.
        - 'situaçao' (opcional): A avaliação do desempenho, que será 'Boa', 'Razoavel' ou 'Ruim' com base na média, se `sit=True`.
    
    Exemplo:
    >> resp = notas(7.8, 8.0, 5.4, 8, sit=True)
    >> print(resp)
    {'Qnt_notas': 4, 'Maior_nota': 8.0, 'Menor_nota': 5.4, 'Media': 7.3, 'situaçao': 'Boa'}
    """

    resp = dict()
    soma = 0

    resp['Qnt_notas'] = len(dados)
    resp['Maior_nota'] = max(dados)
    resp['Menor_nota'] = min(dados)
    resp['Media'] = sum(dados) / len(dados) 
    if sit:
        if resp['Media'] >= 7:
            resp['situaçao'] = 'Boa'
        elif resp['Media'] >= 5:
            resp['situaçao'] = 'razoavel'
        else:
            resp['situaçao'] = 'ruim'

    return resp


resp = notas(7.8, 8.0, 5.4, 8, sit=True)
print(resp)


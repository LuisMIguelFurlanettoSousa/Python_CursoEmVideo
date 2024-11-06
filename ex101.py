def voto(n):
    from datetime import date
    AnoAtual = date.today().year
    idade = AnoAtual - n

    if idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBTIGATORIO.'


print('─' * 30)
nasc = int(input('Qual ano você nasceu?: '))
print(voto(nasc))
palavras = ('Julia', 'Luis', 'Cafe', 'mamao', 'aula',
            'sql', 'estudar', 'guanabara')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')

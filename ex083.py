expr = str(input('Digite a expresao: '))
pilha = list()

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expresao esta correta')
else:
    print('Sua expresao esta errada')
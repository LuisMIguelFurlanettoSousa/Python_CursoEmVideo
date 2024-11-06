frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Essa frase é PALINDROMO')
else:
    print('NÃO é um palindromo')
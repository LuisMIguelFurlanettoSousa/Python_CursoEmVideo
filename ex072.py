numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Qual o numero que voce quer de 0 a 20 ?: '))
    if num >= 0 and num <= 20:
        break
    print('TENTE NOVAMENTE,', end=' ')

print(f'O numero que voce escreveu foi {numeros[num]}')


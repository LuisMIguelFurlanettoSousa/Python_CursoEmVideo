soma = 0
cont = 0

while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1

print(f'A soma dos {cont} numeros é {soma}')

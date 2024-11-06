print('-=' * 20)
print('EMPRESTIMO')
print('-=' * 20)
salario = float(input('Qual o valor do seu salario ?: R$'))
vcasa = float(input('Qual o valor da casa ?: R$'))
anos = int(input('Em quantos anos voçê pretende pagar ?: '))
prestacao = vcasa / (anos * 12)
if prestacao > salario * 30/100:
    print('Voçê NÃO podera pegar o emprestimo, pois o valor que voçê tera que pagar mensalmente sera R${:.2f} e voçê recebe {:.2f}'.format(prestacao, salario))
else:
    print('O valor que voçê pagara por mes sera de R${:.2f} em {} anos, EMPRESTIMO APROVADO '.format(prestacao, anos))

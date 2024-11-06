s = float(input('qual o seu salario ?: R$'))
na = s + (s * (15/100))
print('O seu salario que antes era R${:.2f}, agora com o aumento de 15% sera R${:.2f}'.format(s, na))
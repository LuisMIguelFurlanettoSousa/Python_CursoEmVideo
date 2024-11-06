nome = str(input('Qual o seu nome ?: ')).upper()
if nome == 'LUIS':
    print('Que nome belo em')
elif nome == 'JULIA' or nome == 'CAITANO' or nome == 'FERREIRTA':
    print('esse nome é da minha namorada!!')
elif nome in 'JULIA, LUIS, KEILA, ROGERIO':
    print('conheço')
else:
    print('que nome mais xoxo')
print('Tenha um bom dia, {}!'.format(nome))
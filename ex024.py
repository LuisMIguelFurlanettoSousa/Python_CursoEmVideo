cidade = str(input('qual o nome da sua cidade ?:')).strip()
cidade_split = cidade.split()
print('A sua cidade começa com santo ?: {}'.format('SANTO' in cidade_split[0].upper()))
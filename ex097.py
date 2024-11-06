def mensagem(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))

msg = str(input('Digite uma mensagem: '))
mensagem(msg)
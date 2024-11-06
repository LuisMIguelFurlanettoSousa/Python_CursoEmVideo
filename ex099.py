from time import sleep

def maior(*nums):
    print('-=' * 30)
    print('Analizando os valores passados...')
    for n in nums:
        print(f'{n}',end=' ', flush=True) 
        sleep(0.5)
    print(f'Foram informados {len(nums)} valores ao todo')
    if len(nums) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(nums)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
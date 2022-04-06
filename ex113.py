def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro\033[m')
        except KeyboardInterrupt:
            print('Saindo...')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real\033[m')
        except KeyboardInterrupt:
            print('Saindo...')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
real = leiaFloat('Digite um real: ')
print(f'Inteiro: {num}\nReal: {real}')

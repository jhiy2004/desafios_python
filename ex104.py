def leia_int(msg):
    n = input(msg)
    while not n.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = input(msg)
    return int(n)

n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

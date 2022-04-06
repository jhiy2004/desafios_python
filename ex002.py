def boas_vindas(nome):
    print(f'\033[32mSeja bem vindo, {nome}\033[m')


while True:
    try:
        nome = input('Digite o seu nome: ')
        boas_vindas(nome)
    except KeyboardInterrupt:
        print('\033[33mSaindo...\033[m')
        break

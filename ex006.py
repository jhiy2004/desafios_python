def dobro(n):
    return n*2


def triplo(n):
    return n*3


def raiz_quadrada(n):
    return n**(1/2)


def main():
    try:
        numero = int(input('Digite um número: '))
    except Exception as err:
        print(f'Ocorreu um erro: {err}')
    else:
        print(f'O dobro de {numero} é {dobro(numero)}')
        print(f'O triplo de {numero} é {triplo(numero)}')
        print(f'A raiz quadrada de {numero} é {raiz_quadrada(numero)}')


while True:
    try:
        main()
    except KeyboardInterrupt:
        print('\n\033[31mSaindo...\033[m')
        break

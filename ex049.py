def linha(tam=20):
    print('-'*tam)


def titulo(txt):
    linha()
    print(txt.center(20))
    linha()


def tabuada(numero):
    titulo(f'Tabuada do {numero}')
    for x in range(1, 11):
        res = numero*x
        print(f'\033[32m{numero} X {x} = {res}\033[m')
    linha()


numero = int(input('Digite um número: '))
tabuada(numero)
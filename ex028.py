from random import randint
from time import sleep


def linha(tam=20):
    return '\033[93m'+('-=-'*tam)+'\033[m'


def cabecalho(msg):
    print(linha())
    print(f'\033[34m{msg}\033[m')
    print(linha())


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número inteiro.\033[m')
        else:
            return n


while True:
    try:
        cabecalho('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
        numero_digitado = leia_int('Em que número eu pensei? ')
        while numero_digitado > 5:
            print('\033[31mPor favor digite um número entre 0 e 5.\033[m')
            numero_digitado = leia_int('Em que número eu pensei? ')
    except KeyboardInterrupt:
        print('\n\033[31mSaindo...\033[m')
        break
    else:
        numero_pensado = randint(0, 5)
        print('\033[95mPROCESSANDO...\033[m')
        sleep(1)
        if numero_digitado == numero_pensado:
            print('\033[33mPARABÉNS! Você conseguiu me vencer!')
        else:
            print(
                f'\033[31mGANHEI! Eu pensei no número {numero_pensado} e não no {numero_digitado}!\033[m')

import sys


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mPor favor, digite um número real\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mSaindo...\033[m')
            sys.exit(0)
        else:
            return n


def media(nota1, nota2):
    res = (nota1+nota2)/2
    return res


def main():
    nota1 = leia_float('Digite a primeira nota do aluno: ')
    nota2 = leia_float('Digite a segunda nota do aluno: ')
    print(
        f'\033[32mA média aritmética do aluno foi: {media(nota1,nota2)}\033[m')


while True:
    main()

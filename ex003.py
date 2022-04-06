def soma(n1, n2):
    return n1+n2


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

res = soma(n1, n2)
print(f'\033[32mO resultado da soma entre {n1} e {n2} foi {res}\033[m')

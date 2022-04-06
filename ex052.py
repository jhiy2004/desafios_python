numero = int(input('Digite um número: '))
contador_divisivel = 0
for n in range(1, numero+1):
    if numero % n == 0:
        print(f'\033[32m{n}\033[m', end=' ')
        contador_divisivel += 1
    else:
        print(f'\033[31m{n}\033[m', end=' ')
print(f'\nO número 13 foi divisível {contador_divisivel} vezes')
if contador_divisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
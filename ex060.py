numero = int(input('Digite um número para calcular seu Fatorial: '))
res = 1

print(f'Calculando {numero}! = ', end='')
for n in range(numero,0, -1):
    res *= n
    print(n, end='')
    print(' = ' if n == 1 else ' x ', end = '')
print(res)
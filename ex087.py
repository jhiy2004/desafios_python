matriz = [[],[],[]]
pares = []

for x in range(3):
    for y in range(3):
        num = int(input(f'Digite um valor para [{x},{y}]: '))
        if num % 2 == 0:
            pares.append(num)
        matriz[x].append(num)
print('-='*30)
for x in range(len(matriz)):
    for value in matriz[x]:
        print(f'[{value:^5}]', end=' ')
    print()
print('-='*30)

terceira_coluna = [linha[-1] for linha in matriz]

print(f'A soma dos valores pares é {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(terceira_coluna)}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
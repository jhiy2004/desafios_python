matriz = [[],[],[]]

for x in range(3):
    for y in range(3):
        num = int(input(f'Digite um valor para [{x}, {y}]: '))
        matriz[x].append(num)

for x in range(len(matriz)):
    for value in matriz[x]:
        print(f'[{value:^5}]',end=' ')
    print()  
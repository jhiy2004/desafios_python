numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break

pares = [p for p in numeros if p % 2 == 0]
impares = [i for i in numeros if i % 2 == 1]

print('-='*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

numeros = [[],[]]
for n in range(7):
    num = int(input(f'Digite o {n+1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('-='*30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')

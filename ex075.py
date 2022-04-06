n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

numeros = (n1,n2,n3,n4)
pares = []
print(f'Você digitou os valores: {numeros}')
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição')
print(f'Os valores pares digitados foram: ',end='')
print(*pares)
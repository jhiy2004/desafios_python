maior = 0
menor = 0

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

lista = [numero1, numero2, numero3]

for n in lista:
    menor = lista[0]
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'O maior número digitado foi {max(lista)}')
print(f'O menor número digitado foi {min(lista)}')

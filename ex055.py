maior = 0
menor = 0

for n in range(1, 6):
    peso = float(input(f'Peso da {n}° pessoa: '))
    peso = round(peso, 1)
    if n == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
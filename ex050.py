from ntpath import join


numeros_considerados = []

for n in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_considerados.append(numero)
    
print(f'Os números pares digitados foram:', end = ' ')
if len(numeros_considerados) != 0:
    print(*numeros_considerados, sep = ',')
else:
    print('Nenhum número par foi digitado.')
print(f'A soma entre os números pares digitados foi: {sum(numeros_considerados)}')
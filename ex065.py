maior = 0
menor = 0
opc = 's'
lista = []

while opc in 'Ss':
    num = float(input('Digite um número: '))
    lista.append(num)
    if len(lista) == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    opc = input('Quer continuar? [S/N] ')
print(f'Você digitou {len(lista)} números e a média foi {sum(lista)/len(lista)}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
print('O valor 5 foi encontrado na lista' if 5 in lista else 'O valor 5 não foi encontrado na lista!')
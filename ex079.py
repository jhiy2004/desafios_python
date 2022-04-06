lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado! Não vou adicionar')
    opc = input('Quer continuar? [S/N]').upper()
    while opc not in 'SN':
        opc = input('Tente novamente. Quer continuar? [S/N]').upper()
    if opc in 'N':
        break
print('-='*30)
print(f'Você digitou os valores {lista}')
lista = []

for x in range(5):
    num = int(input('Digite um valor: '))
    if x == 0 or num > max(lista):
        print('Adicionando ao final da lista...')
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print(lista)
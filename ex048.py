lista = []

for i in range(1,501,2):
    if i % 3 == 0:
        lista.append(i)

print(f'A soma de todos os {len(lista)} valores solicitados é {sum(lista)}')
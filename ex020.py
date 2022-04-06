from random import shuffle

nomes = []

nomes.append(input('Digite o primeiro nome: '))
nomes.append(input('Digite o segundo nome: '))
nomes.append(input('Digite o terceiro nome: '))
nomes.append(input('Digite o quarto nome: '))

lista_embaralhada = shuffle(nomes)

print(f'A ordem de apresentação será: \n{nomes}')

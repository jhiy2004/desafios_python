pessoas = []
pesados = []
leves = []

while True:
    nome = input('Nome: ')
    peso = input('Peso: ')
    pessoa = [peso, nome]
    pessoas.append(pessoa)
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break

pessoas.sort(reverse=True)
for c in range(0, len(pessoas)):
    if pessoas[0][0] == pessoas[c][0]:
        pesados.append(pessoas[c][1])
    elif pessoas[-1][0] == pessoas[c][0]:
        leves.append(pessoas[c][1]) 

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {pessoas[0][0]:.1f}Kg. Peso de {pesados}')
print(f'O menor peso foi de {pessoas[-1][0]:.1f}Kg. Peso de {leves}')
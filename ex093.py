gols = []
nome = input('Nome do Jogador: ')
qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
for p in range(1, qtd_partidas+1):
    gol = int(input(f'Quantos gols na partida {p}? '))
    gols.append(gol)
jogador = {'nome': nome, 'gols': gols, 'total': sum(gols)}

print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
p=1
for g in gols:
    print(f' => Na partida {p}, fez {g} gols.')
    p+=1
print(f"Foi um total de {jogador['total']}")
jogadores = list()

while True: 
    gols = []
    nome = input('Nome do Jogador: ')
    qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for p in range(1, qtd_partidas+1):
        gol = int(input(f'Quantos gols na partida {p}? '))
        gols.append(gol)
    jogador = {'nome': nome, 'gols': gols, 'total': sum(gols)}
    jogadores.append(jogador)
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
        print('ERRO!, digite apenas S ou N.')
    if opc == 'N':
        break
print('-='*30)
print('cod ', end=' ')
for i in jogadores[0].keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if escolha == 999:
        break
    elif escolha >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {escolha}!')
    else:
        escolhido = jogadores[escolha]
        print(f"-- LEVANTAMENTO DO JOGADOR {escolhido['nome']}")
        p = 1
        for g in escolhido['gols']:
            print(f'    No jogo {p} fez {g} gols.')
            p += 1
    print('-'*60)
print('<< VOLTE SEMPRE >>')

from random import randint
from time import sleep

jogos = []
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('SORTEANDO 10 JOGOS')

for x in range(qtd_jogos):
    jogo = []
    for y in range(6):
        jogo.append(randint(1,60))
    jogos.append(jogo)

for num,jogo in enumerate(jogos):
    print(f'Jogo {num+1}: {jogo}')
    sleep(.7)
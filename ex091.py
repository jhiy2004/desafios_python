from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}

for n in range(1,5): 
    jogadores[f'Jogador {n}'] = randint(1,6)

print('Valores sorteados:')
for k,v in jogadores.items():
    print(f"Jogador {k} tirou {v} no dado.")
    sleep(.7)

print('-='*30)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
p = 1
for j in ranking:
    print(f'{p}° lugar: {j[0]} com {j[1]} no dado.')
    p+=1 

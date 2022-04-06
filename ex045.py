from random import randint
from time import sleep
from random import randint

i = 0
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
print('Suas opções: ')
for n in jokenpo:
    print(f'[ {i} ] {n}')
    i += 1
opcao_jogador = int(input('Qual é a sua jogada? '))
opcao_computador = randint(0, 2)

print('JO')
sleep(.7)
print('KEN')
sleep(.7)
print('PO!!!')

print('-='*15)
print(f'Jogador jogou {jokenpo[opcao_jogador]}')
print(f'Computador jogou {jokenpo[opcao_computador]}')
print('-='*15)

if opcao_jogador == opcao_computador:
    print('EMPATE')
elif opcao_jogador == 0 and opcao_computador == 1:
    print('COMPUTADOR VENCE')
elif opcao_jogador == 0 and opcao_computador == 2:
    print('JOGADOR VENCE')
elif opcao_jogador == 1 and opcao_computador == 0:
    print('JOGADOR VENCE')
elif opcao_jogador == 1 and opcao_computador == 2:
    print('COMPUTADOR VENCE')
elif opcao_jogador == 2 and opcao_computador == 0:
    print('COMPUTADOR VENCE')
elif opcao_jogador == 2 and opcao_computador == 1:
    print('JOGADOR VENCE')
else:
    print('JOGADA INVÁLIDA')

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
''')
numero_computador = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    numero_jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if numero_jogador == numero_computador:
        acertou = True
    if numero_computador > numero_jogador:
        print('Mais... Tente mais uma vez.')
    elif numero_computador < numero_jogador:
        print('Menos... Tente mais uma vez.')

print(f'Acertou com {tentativas} tentativas. Parabéns')
from random import randint

contador = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:
    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = input('Par ou Ímpar? [P/I] ').upper()
    num_jogador = int(input('Diga um valor: '))

    if escolha_jogador == 'P':
        escolha_computador = 'I'
    else:
        escolha_computador = 'P'
    num_computador = randint(1,10)

    total = num_jogador + num_computador
    print('-'*30)
    print(f'Você jogou {num_jogador} e o computador {num_computador}. Total de {total} DEU PAR',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-'*30)
    if total % 2 == 0 and escolha_jogador == 'P':
        print('Você VENCEU!')
        contador += 1
    elif total % 2 != 0 and escolha_jogador == 'I':
        print('Você VENCEU!')
        contador += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print('=-'*15)
print(f'GAME OVER! Você venceu {contador} vezes.')
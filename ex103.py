nome = input('Nome do jogador: ')
gols = input('Número de Gols: ')

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols not in '0123456789':
        gols = '0'
    return 'O jogador {} fez {} gol(s) no campeonato.'.format(nome, gols)

print('-'*30)
print(ficha(nome, gols))
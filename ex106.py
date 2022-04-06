CORES = ('\033[m',
         '\033[0;30;41m',
         '\033[0;30;42m',
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[7;30m'
)

def cabecalho(titulo, cor=0):
    tam = len(titulo)+2
    print(CORES[cor], end='')
    print('~'*tam)
    print(titulo.center(tam))
    print('~'*tam)
    print(CORES[0], end='')

while True:
    cabecalho('SISTEMA DE AJUDA PyHELP',2)
    pergunta = input('Função ou Biblioteca > ')
    if pergunta == 'fim':
        break
    print(CORES[6], end='')
    help(pergunta)
    print(CORES[0],end='')

cabecalho('ATÉ LOGO!',1)
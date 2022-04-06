from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'pessoas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar pessoas cadastradas',
                    'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo de texto
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        cadastrar(arquivo)
        print('Cadastrar nova pessoa')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
    sleep(1)

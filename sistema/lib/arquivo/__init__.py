from dataclasses import replace
from fileinput import close
from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()
        with open(nome,'rt') as f:
            if len(f.readlines()) < 1:
                print('Parece que ainda não existe nenhum registro, tente cadastrar uma nova pessoa')
            f.close()

def cadastrar(arq):
    nome = input('Nome: ')
    idade = leiaInt('Idade: ')
    try:
        a = open(arq, 'at')
    except Exception:
        print('\033[31mHouve um ERRO na abertura do arquivo![m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception:
            print('\033[31mHouve um ERRO na escrita do arquivo![m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
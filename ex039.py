from datetime import date


def verifica_alistamento(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o alistamento.')
        print(f'Seu alistamento será em {ano_nascimento + 18}.')
    elif idade > 18:
        print(
            f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
        print(
            f'Você já deveria ter se alistado há {ano_atual-(ano_nascimento+18)} anos.')
        print(f'Seu alistamento foi em {ano_nascimento+18}')
    else:
        print(
            f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
        print('Você tem que se alistar IMEDIATAMENTE!.')


sexo = input(
    'Você é do sexo \033[34mmasculino\033[m ou \033[31mfeminino\033[m? ')
if sexo == 'feminino':
    print('Você não precisa fazer alistamento militar.')
else:
    ano_nascimento = int(input('Ano de nascimento: '))
    verifica_alistamento(ano_nascimento)

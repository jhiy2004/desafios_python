from datetime import date

ano_atual = date.today().year

nome = input('Nome: ')
ano_nascimento = int(input('Ano de Nascimento: '))
carteira_trabalho = int(input('Carteira de Trabalho (0 não tem): '))
trabalhador = {'nome': nome, 'idade': ano_atual - ano_nascimento, 'ctps': carteira_trabalho}
if carteira_trabalho != 0:
    trabalhador['contratação'] = int(input('Ano de contratacao: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação']+ 35) - ano_atual)
print('-='*30)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')

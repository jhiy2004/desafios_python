from random import choice

alunos = []

alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))

escolhido = choice(alunos)
print(f'O aluno sorteado foi: {escolhido}')

def media(n1,n2):
    return (n1 + n2)/2

alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno = [nome, [nota1,nota2], media(nota1, nota2)]
    alunos.append(aluno)
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break
print('-='*30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
for num,aluno in enumerate(alunos):
    print(f'{num:<4}{aluno[0]:<10}{aluno[-1]:>8.1f}')

while True:
    print('-'*30)
    mostrar = int(input('Mostrar notas de qual aluno? '))
    if mostrar == 999:
        break
    print(f'Notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}')
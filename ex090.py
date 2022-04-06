nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
if media < 5:
    situacao = 'Reprovado'
elif media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Recuperação'
print('-='*30)
aluno = {'nome': nome, 'media': media, 'situacao': situacao}
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
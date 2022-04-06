pessoas = []
pessoas_acima_media = []
mulheres = []
total_idade = 0

while True:
    nome = input('Nome: ')
    while True:
        sexo = input('Sexo: [M/F] ').upper()
        if sexo in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    idade = int(input('Idade: '))
    while True:
        opc = input('Quer continuar? [S/N] ').upper()
        if opc in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)
    total_idade += idade
    if opc == 'N':
        break
media = total_idade / len(pessoas)
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p)
    if p['idade'] > media:
        pessoas_acima_media.append(p)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos')
print(f'C) As mulheres cadastradas foram ',end='')
for m in mulheres:
    print(m['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for pa in pessoas_acima_media:
    for k,v in pa.items():
        print(f'{k} = {v}', end='; ')
    print()
print('<< ENCERRADO >>')
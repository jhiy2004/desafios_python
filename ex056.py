pessoas = []
idades = []
maior_idade = 0
nome_maior_idade = ''
mulheres_menos_vinte = 0

for n in range(1,5):
    print(f'-----{n}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    pessoa = (nome, idade, sexo)
    pessoas.append(pessoa)

for p in pessoas:
    idades.append(p[1])
    if p[2] == 'M':
        if p[1] > maior_idade:
            maior_idade = p[1]
            nome_maior_idade = p[0]
    if p[2] == 'F':
        if p[1] < 20:
            mulheres_menos_vinte += 1
    
print(f'A média de idade do grupo é de {round((sum(idades)/4), 1)} anos.')
print(f'O homem mais velho tem {maior_idade} e se chama {nome_maior_idade}.')
print(f'Ao todos são {mulheres_menos_vinte} com menos de 20 anos.')    

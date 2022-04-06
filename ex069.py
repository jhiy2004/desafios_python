maiores = homens = mulheres =0
pessoas = []
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper()
    pessoa = (idade, sexo)
    pessoas.append(pessoa)
    print('-'*30)
    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break
for p in pessoas:
    if p[0] > 18:
        maiores += 1
    if p[1] == 'M':
        homens += 1
    if p[1] == 'F' and p[0] < 20:
        mulheres += 1
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
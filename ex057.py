sexos = ['F', 'M']

sexo = input('Informe seu sexo[M/F]: ').upper()

while sexo not in sexos:
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ')
print(f'Sexo {sexo} registrado com sucesso')
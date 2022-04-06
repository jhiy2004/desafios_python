nome = input('Digite o seu nome completo: ')
primeiro_nome = nome.split(' ')[0]
espacos = nome.count(' ')

print(f'Seu nome em letras maiúsculas fica: {nome.upper()}')
print(f'Seu nome em letras minúsculas fica: {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - espacos} letras')
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')
